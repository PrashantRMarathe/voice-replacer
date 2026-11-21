"""Wrap one JPEG into a single-page A4 PDF (no dependencies).
  python narration/jpg_to_pdf.py in.jpg out.pdf
"""
import struct
import sys
from pathlib import Path


def jpeg_size(data: bytes):
    i = 2
    while i < len(data):
        marker, length = data[i + 1], struct.unpack(">H", data[i + 2:i + 4])[0]
        if 0xC0 <= marker <= 0xCF and marker not in (0xC4, 0xC8, 0xCC):
            h, w = struct.unpack(">HH", data[i + 5:i + 9])
            return w, h
        i += 2 + length
    raise ValueError("not a JPEG")


src, dst = Path(sys.argv[1]), Path(sys.argv[2])
img = src.read_bytes()
w, h = jpeg_size(img)
PW, PH = 595.28, 841.89  # A4 in points
content = f"q {PW} 0 0 {PH} 0 0 cm /Im0 Do Q".encode()
objs = [
    b"<< /Type /Catalog /Pages 2 0 R >>",
    b"<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
    f"<< /Type /Page /Parent 2 0 R /MediaBox [0 0 {PW} {PH}] /Resources << /XObject << /Im0 4 0 R >> >> /Contents 5 0 R >>".encode(),
    f"<< /Type /XObject /Subtype /Image /Width {w} /Height {h} /ColorSpace /DeviceRGB /BitsPerComponent 8 /Filter /DCTDecode /Length {len(img)} >>\nstream\n".encode() + img + b"\nendstream",
    f"<< /Length {len(content)} >>\nstream\n".encode() + content + b"\nendstream",
]
out = bytearray(b"%PDF-1.4\n")
offsets = []
for n, body in enumerate(objs, 1):
    offsets.append(len(out))
    out += f"{n} 0 obj\n".encode() + body + b"\nendobj\n"
xref = len(out)
out += f"xref\n0 {len(objs) + 1}\n0000000000 65535 f \n".encode()
out += b"".join(f"{o:010d} 00000 n \n".encode() for o in offsets)
out += f"trailer\n<< /Size {len(objs) + 1} /Root 1 0 R >>\nstartxref\n{xref}\n%%EOF\n".encode()
dst.write_bytes(out)
print(f"{dst} ({w}x{h} image, {len(out) // 1024} KB)")
