import os
import shutil
import sys
from pathlib import Path

MAX_BYTES = 1_048_576
SRC = Path(__file__).resolve().parent / "assets" / "entry.png"


def main():
    data = SRC.read_bytes()
    if data[:2] != b"\xff\xd8":
        sys.exit("assets/entry.png is not a JPEG (missing FFD8)")
    if len(data) > MAX_BYTES:
        sys.exit("assets/entry.png is larger than 1,048,576 bytes")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    shutil.copyfile(SRC, out_dir / "entry.png")
    print(f"wrote {out_dir / 'entry.png'} ({len(data)} bytes)")


if __name__ == "__main__":
    main()
