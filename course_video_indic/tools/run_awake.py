"""Run a command while holding Windows awake (same call as the English watch_drive.py).
A closed lid still sleeps.

  python tools/run_awake.py bash scripts/render_lesson.sh hindi A3ProblemSolvingHi
"""
import ctypes
import subprocess
import sys

ES_CONTINUOUS, ES_SYSTEM_REQUIRED = 0x80000000, 0x00000001
ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS | ES_SYSTEM_REQUIRED)
try:
    code = subprocess.call(sys.argv[1:])
finally:
    ctypes.windll.kernel32.SetThreadExecutionState(ES_CONTINUOUS)
sys.exit(code)
