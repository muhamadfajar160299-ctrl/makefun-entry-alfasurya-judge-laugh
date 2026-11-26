"""Write the competition entry (one office-life joke) to entry.txt.

The entry is a single line about office life, under 200 characters.
The program writes it verbatim to
``$MAKEFUN_OUTPUT_DIR/entry.txt`` (default ``/output``).
"""

import os

ENTRY = "I asked IT for a faster laptop; they gave me a shorter deadline instead."

OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main():
    if not ENTRY.strip():
        raise ValueError("entry text must not be empty")
    try:
        os.makedirs(OUTPUT_DIR, exist_ok=True)
        with open(os.path.join(OUTPUT_DIR, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        raise SystemExit("failed to write entry.txt: %s" % exc)


if __name__ == "__main__":
    main()
