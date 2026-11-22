"""Entry for the make.fun bounty "Make the AI judge feel curious".

Writes a single short text (1-280 characters) to /output/entry.txt.
Deterministic, stdlib only, no network.
"""

import os
from pathlib import Path

TEXT = (
    "Somewhere down the lane, a door stands half open, warm light spilling "
    "onto the stones. No one is inside, yet a kettle hums, and a chair waits "
    "by the window, as if someone just stepped out and left the evening "
    "listening for their return."
)


def main() -> None:
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
