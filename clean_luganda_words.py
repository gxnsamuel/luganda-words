#!/usr/bin/env python3
"""
clean_luganda_words.py

Reads a raw text file, extracts words, lowercases them, removes duplicates,
sorts alphabetically, and writes a clean word list (one word per line).

Usage:
    python3 clean_luganda_words.py input.txt output.txt
"""

import sys
import re
import unicodedata

# Luganda uses standard Latin letters plus occasional apostrophe (ng'),
# so we keep letters and apostrophes, and split on everything else.
WORD_PATTERN = re.compile(r"[a-zA-Z']+")


def extract_words(text: str):
    """Pull out word-like tokens from raw text."""
    raw_words = WORD_PATTERN.findall(text)
    cleaned = []
    for w in raw_words:
        w = w.strip("'")          # drop stray leading/trailing apostrophes
        w = w.lower()
        if not w:
            continue
        if len(w) == 1 and w not in ("n", "'"):
            # skip stray single letters (likely OCR/typo noise),
            # but keep single "n" since it can be a valid Luganda prefix/word
            continue
        cleaned.append(w)
    return cleaned


def sort_key(word: str):
    """Alphabetical sort that treats accented/special chars sensibly."""
    normalized = unicodedata.normalize("NFKD", word)
    return normalized


def main():
    if len(sys.argv) != 3:
        print("Usage: python3 clean_luganda_words.py input.txt output.txt")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    with open(input_path, "r", encoding="utf-8", errors="ignore") as f:
        text = f.read()

    words = extract_words(text)
    unique_words = sorted(set(words), key=sort_key)

    with open(output_path, "w", encoding="utf-8") as f:
        for w in unique_words:
            f.write(w + "\n")

    print(f"Read {len(words)} word occurrences.")
    print(f"Wrote {len(unique_words)} unique, sorted words to {output_path}")


if __name__ == "__main__":
    main()
