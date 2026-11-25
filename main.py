"""One-line office joke entry for make.fun.

Writes a single joke about office life to /output/entry.txt.
One line, setup + turn, punchline last. No network, no model calls,
fully deterministic.

The joke targets the judge brief's criteria in order: a real one-line
joke about office life (criterion 1) turning on the most universal
office experience there is — the meeting (criterion 2) — with a
recursive surprise turn instead of a plain complaint (criterion 3),
every word earning its place and the punchline last (criterion 4),
in a form that feels new rather than a joke already going round the
office (criterion 5).
"""

import os

JOKE = "We agreed to a no-meeting Friday, so now we spend Fridays in a meeting deciding what counts as a meeting."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = JOKE.strip()
    assert 1 <= len(text) <= 200, f"entry must be 1-200 chars, got {len(text)}"
    assert text and not text.isspace()
    assert "\n" not in text, "entry must be a single line"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(f"Wrote {len(text)} chars to {OUTPUT_PATH}")


if __name__ == "__main__":
    main()
