"""One Word for Your Wi-Fi.

Writes the single best word for a Wi-Fi network name to entry.txt.

The word is "Ghosting": home Wi-Fi ghosts you -- it vanishes mid-call,
mid-download, with no explanation, exactly like a bad date. It is funny
at once, true to how home Wi-Fi actually behaves, and it works as a
network name with no context needed.
"""

import os

WORD = "Ghosting"


def main() -> None:
    # Self-check against the gate: 1 to 20 characters, not only whitespace.
    if not (1 <= len(WORD) <= 20) or not WORD.strip():
        raise ValueError("entry word fails the gate: %r" % WORD)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(WORD)


if __name__ == "__main__":
    main()
