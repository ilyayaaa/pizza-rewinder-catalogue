from pathlib import Path
from PIL import Image

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "assets" / "source.png"
DST = ROOT / "assets" / "entry.png"  # JPEG bytes despite the name
LIMIT = 1_000_000

img = Image.open(SRC).convert("RGB").resize((1024, 1024), Image.LANCZOS)
for q in range(95, 65, -5):
    img.save(DST, format="JPEG", quality=q)
    size = DST.stat().st_size
    if size <= LIMIT:
        break
print(f"quality={q} size={size}")
