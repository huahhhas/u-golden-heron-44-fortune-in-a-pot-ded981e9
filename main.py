#!/usr/bin/env python3
"""Fortune in a Pot — writes one kind, funny fortune for a houseplant.

Writes the fortune to $OUTPUT_DIR/entry.txt (default /output) with no
trailing newline, then self-verifies the written file:
UTF-8, 1-120 characters, not only whitespace, exact match, no trailing
newline, byte-identical to the expected bytes.
"""

import hashlib
import os
import sys

LINE = "Your leaves reach for the sun every morning, and the windowsill has already decided you are its favourite tenant."
MAX_CHARS = 120


def main() -> int:
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")

    expected = LINE.encode("utf-8")
    with open(path, "wb") as f:
        f.write(expected)

    # Self-verification.
    with open(path, "rb") as f:
        data = f.read()
    text = data.decode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= MAX_CHARS, f"length {len(text)} out of gate"
    assert text.strip(), "entry is only whitespace"
    assert not text.endswith("\n"), "trailing newline present"
    assert data == expected, "written bytes differ from expected"
    assert "\n" not in text, "entry must be a single line"
    print(f"entry.txt OK: {len(text)} chars, "
          f"sha256={hashlib.sha256(data).hexdigest()}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
