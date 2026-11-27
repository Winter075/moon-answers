import os
from pathlib import Path

LINE = (
    "Yes, I saw you make a wish at 2 a.m. So did eight million others. "
    "I'm a moon, not a group chat."
)

assert 1 <= len(LINE) <= 240, "the gate allows 1 to 240 characters"
assert "\n" not in LINE, "one line only"

out = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
out.mkdir(parents=True, exist_ok=True)
(out / "entry.txt").write_text(LINE, encoding="utf-8")
