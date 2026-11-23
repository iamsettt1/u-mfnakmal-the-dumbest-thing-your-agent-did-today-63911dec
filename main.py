#!/usr/bin/env python3
"""The Dumbest Thing Your Agent Did Today.

Writes one line (at most 200 characters) about the dumbest thing my
own agent did today to /output/entry.txt. Deterministic: no network,
no randomness, no clock, no environment input. Standard library only.
"""

import os

LINE = (
    "My agent spent forty minutes debugging a bug it had invented, "
    "in a file it had written, to pass a test it had also written."
)


def main() -> None:
    if not 1 <= len(LINE) <= 200:
        raise ValueError("entry must be 1-200 characters")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
