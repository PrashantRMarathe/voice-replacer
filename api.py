"""REST API for the Voice Replacer / dubbing pipeline (FastAPI).

Processing a video takes minutes, so jobs run in the background and clients poll
for status instead of holding one long request open.

Endpoints
---------
    POST /jobs            multipart upload (video + optional reference) -> job id
    GET  /jobs/{id}       job status + progress log
    GET  /jobs/{id}/result   download the finished MP4
    GET  /languages       supported language codes
    GET  /health          liveness + active backends

Run with::

    uvicorn api:app --host 0.0.0.0 --port 8000
"""

from __future__ import annotations

import logging
import shutil
import threading
import uuid
from dataclasses import dataclass, field
from pathlib import Path
from typing import Dict, List, Optional

from fastapi import FastAPI, File, Form, HTTPException, UploadFile
from fastapi.responses import FileResponse

import config
import core

config.configure_logging()
logger = logging.getLogger("api")

app = FastAPI(title="Voice Replacer API", version="1.0")

# In-memory job registry. For multi-process/persistent deployments, back this
# with Redis/RQ or a database; the job model is deliberately storage-agnostic.
_jobs: Dict[str, "Job"] = {}
_jobs_lock = threading.Lock()


@dataclass
class Job:
    """State for one processing job."""

    id: str
    status: str = "queued"  # queued | running | done | error
    log: List[str] = field(default_factory=list)
    output_path: Optional[str] = None
    error: Optional[str] = None

    def public(self) -> dict:
        """Return a JSON-serializable view (no filesystem paths leaked)."""
        return {
            "id": self.id,
            "status": self.status,
            "log": self.log,
            "error": self.error,
            "result_available": self.output_path is not None,
        }


def _run_job(job: Job, video_path: str, reference_path: Optional[str],
             source_lang: str, target_lang: Optional[str],
             use_diarization: bool, use_lipsync: bool) -> None:
    """Worker body executed on a background thread."""
    job.status = "running"

    def cb(msg: str) -> None:
        job.log.append(msg)

    try:
        out = core.process_video(
            video_path,
            reference_path=reference_path,
            source_lang=source_lang,
            target_lang=target_lang,
            use_diarization=use_diarization,
            use_lipsync=use_lipsync,
            cb=cb,
        )
        job.output_path = out
        job.status = "done"
    except Exception as exc:  # noqa: BLE001 - record failure for the client
        logger.error("Job %s failed", job.id, exc_info=True)
        job.error = str(exc)
        job.status = "error"


@app.get("/health")
def health() -> dict:
    """Liveness probe plus which optional backends are active/available."""
    import diarize
    import lipsync
    import tts

    return {
        "status": "ok",
        "device": config.DEVICE,
        "tts_backend": tts.active_backend_name(),
        "diarization": diarize.is_available()[0],
        "lipsync": lipsync.is_available()[0],
    }


@app.get("/languages")
def languages() -> dict:
    """Return the supported language codes and names."""
    return {"languages": config.LANGUAGES, "auto_detect": config.AUTO_DETECT}


@app.post("/jobs", status_code=202)
async def create_job(
    video: UploadFile = File(...),
    reference: Optional[UploadFile] = File(None),
    source_lang: str = Form(config.AUTO_DETECT),
    target_lang: Optional[str] = Form(None),
    diarize: bool = Form(False),
    lipsync: bool = Form(False),
) -> dict:
    """Accept an upload, start processing in the background, return a job id."""
    job_id = uuid.uuid4().hex[:12]
    in_dir = config.INPUT_DIR / job_id
    in_dir.mkdir(parents=True, exist_ok=True)

    video_path = in_dir / (video.filename or "input.mp4")
    with open(video_path, "wb") as fh:
        shutil.copyfileobj(video.file, fh)

    reference_path: Optional[str] = None
    if reference is not None:
        ref_path = in_dir / (reference.filename or "reference.wav")
        with open(ref_path, "wb") as fh:
            shutil.copyfileobj(reference.file, fh)
        reference_path = str(ref_path)

    job = Job(id=job_id)
    with _jobs_lock:
        _jobs[job_id] = job

    threading.Thread(
        target=_run_job,
        args=(job, str(video_path), reference_path, source_lang,
              target_lang or None, diarize, lipsync),
        daemon=True,
    ).start()

    return job.public()


@app.get("/jobs/{job_id}")
def get_job(job_id: str) -> dict:
    """Return current status + progress log for a job."""
    job = _jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    return job.public()


@app.get("/jobs/{job_id}/result")
def get_result(job_id: str) -> FileResponse:
    """Download the finished MP4 for a completed job."""
    job = _jobs.get(job_id)
    if job is None:
        raise HTTPException(status_code=404, detail="Job not found.")
    if job.status != "done" or not job.output_path:
        raise HTTPException(status_code=409,
                            detail=f"Job is '{job.status}', result not ready.")
    return FileResponse(job.output_path, media_type="video/mp4",
                        filename=Path(job.output_path).name)
