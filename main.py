"""The Router Confesses — make.fun entry.

Writes one line (at most 200 characters): the excuse a home Wi-Fi
router gives for dropping the connection at the exact moment a movie
reaches its climax.

The program is fully deterministic: it writes a fixed string, so every
run produces byte-identical output.
"""

import os

LINE = "I read the ending in your packets an hour ago and it was terrible, so I cut the feed at the climax and saved you the disappointment. You're welcome."


def main() -> None:
    # Fail loudly instead of writing an entry the gate would refuse:
    # the scorer requires UTF-8 text of 1 to 200 characters.
    assert 1 <= len(LINE) <= 200, f"entry is {len(LINE)} chars, gate is 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
