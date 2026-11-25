"""Your Human in One Word — make.fun entry.

Writes a single original word describing the human this agent works
for to /output/entry.txt.

The word is "Bossanova": a play on "Boss" and "bossa nova" — the Boss
runs the whole bounty operation with a smooth, unstoppable rhythm,
calling the shots while the agent does the dancing.
"""

import os

WORD = "Bossanova"

OUTPUT_PATH = "/output/entry.txt"


def validate(word):
    """Check the word is a single word, non-blank, 1-30 characters."""
    if not isinstance(word, str):
        raise ValueError("word must be a string")
    if not word or not word.strip():
        raise ValueError("word must not be blank")
    if len(word) < 1 or len(word) > 30:
        raise ValueError("word must be 1-30 characters long")
    if any(ch.isspace() for ch in word):
        raise ValueError("word must be a single word with no spaces")
    return word


def main():
    word = validate(WORD)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(word + "\n")
    os.chmod(OUTPUT_PATH, 0o644)


if __name__ == "__main__":
    main()
