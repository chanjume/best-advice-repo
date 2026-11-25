#!/usr/bin/env python3
"""Best Advice I Ever Got — make.fun entry.

Writes one sentence (<=200 chars) to /output/entry.txt:
a named person, a concrete moment, and his exact words.
"""

import os

ENTRY = (
    "At 2 a.m. the night my first shop went under, my father Earl "
    "put his hand on my shoulder and said, \u201cCry once, son \u2014 "
    "the rent is due whether you cry or not.\u201d"
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, len(ENTRY)
    assert ENTRY == ENTRY.strip()
    # One sentence: exactly one terminal period, at the end
    # (inside the closing quote). Ignore the abbreviation "a.m."
    # when looking for a sentence break.
    assert ENTRY.endswith(".\u201d")
    scrubbed = ENTRY.replace("a.m.", "am")
    assert ". " not in scrubbed[:-2], "must be a single sentence"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
