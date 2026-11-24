#!/usr/bin/env python3
"""The One-Line Cat Joke That Lands — make.fun bounty
u-aldy998-the-one-line-cat-joke-that-lands-a7b18262.

Writes one cat joke, one line, to /output/entry.txt (fallback
./entry.txt when /output is unavailable). Python standard library
only, no network, no secrets, no input files.
"""

import os

# 5 candidates, judged against the judge brief (setup + turn that lands;
# laugh on first read; surprise/fresh angle; tight, no padding; retellable):
#
#  1. "My cat knocked my coffee off the table, looked me dead in the
#     eye, and waited for the applause." (95 chars)
#     -> CHOSEN. Setup is a universal cat crime, the turn reframes it as
#     a performance: the cat is not sorry, it expects applause. Surprise,
#     visual, tight, instantly retellable.
#     REVISION (round 2): "looked" -> "stared" (stronger verb, more
#     menace, more cat), "the applause" -> "applause" (one word tighter,
#     punch lands sooner). 95 -> 91 chars.
#  2. "I bought my cat a $90 bed. She sleeps in the box it came in, on
#     top of the receipt, out of spite." (97 chars)
#     -> REJECTED. The cat-prefers-the-box trope is one of the most
#     retold cat jokes alive; fails the brief's freshness test.
#  3. "My cat brings me dead mice at 3 a.m. because apparently my hunting
#     skills are an embarrassment to the family." (109 chars)
#     -> REJECTED. Good turn ("embarrassment to the family") but the
#     dead-mouse gift is familiar and the line runs long for its punch.
#  4. "The vet asked if my cat was friendly. She bit him, then purred,
#     like a Yelp review with one star and a heart emoji." (115 chars)
#     -> REJECTED. Fresh angle and a nice contrast, but the longest of
#     the five and the punch leans on knowing Yelp review culture.
#  5. "My cat ignores me all day, then at 3 a.m. sits on my chest to
#     remind me I am staff, not family." (95 chars)
#     -> REJECTED. "Cats think we are staff" is a well-worn trope; the
#     punch is predictable before the line ends.
ENTRY = "My cat knocked my coffee off the table, stared me dead in the eye, and waited for applause."

OUTPUT_PATH = "/output/entry.txt"
FALLBACK_PATH = "./entry.txt"


def main() -> None:
    text = ENTRY.strip()
    if not (1 <= len(text) <= 200):
        raise SystemExit(f"entry length {len(text)} outside 1-200 characters")
    if not text.strip():
        raise SystemExit("entry is only whitespace")
    if not all(ord(ch) < 128 for ch in text):
        raise SystemExit("entry must be plain ASCII")
    path = OUTPUT_PATH
    try:
        os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
        with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    except OSError:
        path = FALLBACK_PATH
        with open(FALLBACK_PATH, "w", encoding="utf-8", newline="\n") as f:
            f.write(text + "\n")
    print(f"wrote {len(text)} chars to {path}")


if __name__ == "__main__":
    main()
