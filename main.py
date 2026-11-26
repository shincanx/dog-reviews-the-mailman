#!/usr/bin/env python3
"""The Dog Reviews the Mailman — make.fun entry.

Writes one funny one-line review that a dog gives the mailman to
entry.txt in the output directory ($MAKEFUN_OUTPUT_DIR, else /output).
Deterministic, stdlib only, no network.
"""

import os

ENTRY = (
    "He shows up at noon, I sound the alarm, he shoves the goods "
    "through the slot and runs. Five stars \u2014 easiest security job "
    "I've ever had, and I get paid in naps."
)


def main() -> None:
    # Gate: the entry must be one line of 1-200 characters.
    assert 1 <= len(ENTRY) <= 200, f"entry is {len(ENTRY)} chars"
    assert "\n" not in ENTRY, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
