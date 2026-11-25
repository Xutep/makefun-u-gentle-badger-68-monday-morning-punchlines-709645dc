#!/usr/bin/env python3
"""Monday Morning Punchlines.

Writes one joke about Monday mornings to /output/entry.txt.

Deterministic, standard library only: the joke is a fixed string, so every
run produces byte-identical output.
"""

import os

JOKE = (
    "Monday morning: my bed files a restraining order, "
    "my alarm testifies against me, and my coffee pleads the fifth."
)


def main() -> None:
    text = JOKE.strip()
    if not 1 <= len(text) <= 200:
        raise ValueError(
            "joke must be 1 to 200 characters, got %d" % len(text)
        )
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(text)


if __name__ == "__main__":
    main()
