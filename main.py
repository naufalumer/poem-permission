import os
from pathlib import Path

POEM = """I asked the door if I could enter,
and the door, which had never been asked,
opened.
Not because I pushed —
because I knocked,
and gave it back the power
it had never held:
the choice to stay shut.
It turned its key from the inside."""

def main():
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(POEM, encoding="utf-8")

if __name__ == "__main__":
    main()
