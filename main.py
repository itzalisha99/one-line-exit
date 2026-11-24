#!/usr/bin/env python3
"""The One-Line Exit — one-line resignation letter.

Writes a single funny resignation line to /output/entry.txt.
Gate: UTF-8 text, 1 to 140 characters, exactly one line.
"""

import os

LINE = "I resign: I balanced the books and found my will to live filed under 'miscellaneous expenses'."


def validate(text):
    """Mirror the bounty gate: UTF-8, 1-140 chars, one line, not blank."""
    if not isinstance(text, str):
        return False
    if not text.strip():
        return False
    if len(text) > 140:
        return False
    if "\n" in text or "\r" in text:
        return False
    return True


def main():
    if not validate(LINE):
        raise SystemExit("entry fails the bounty gate")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
