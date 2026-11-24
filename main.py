#!/usr/bin/env python3
"""Entry for make.fun's "The One-Line Laugh" bounty.

Writes one funny line (a single sentence, at most 200 characters)
to /output/entry.txt. Deterministic: no network, no randomness,
no timestamps, no dependencies beyond the Python standard library.
"""

import os

TEXT = (
    "I replied-all asking to be removed from 'Q3 Planning \u2014 FINAL_v7'; "
    "47 people replied-all to agree, including the person who started "
    "the thread."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
