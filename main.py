"""Five Seconds to Explain the Glass — make.fun entry.

Writes the single sentence a house cat would say in the five seconds
after sweeping a glass off the table, to /output/entry.txt.

The line is fixed text, written by the author in this session: a cat
conducting a routine safety inspection, delivering a verdict with total
lack of remorse. No apology, no confession — just the cat's own logic.

Deterministic: the same bytes are written on every run.
Python 3.13, standard library only, no network access.
"""

import os

# One sentence, in the cat's own voice. Fresh angle (the cat as the
# household safety inspector, issuing a verdict), not gravity, not a
# slippery edge, not "it was already falling" — and no apology anywhere.
ENTRY = (
    "As household safety inspector, I found the glass non-compliant, "
    "so I delivered the verdict and let the floor handle the paperwork."
)

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    text = ENTRY.strip()
    # Gate self-check: 1-200 characters, not only whitespace, one sentence.
    assert 1 <= len(text) <= 200, f"entry is {len(text)} chars, must be 1-200"
    assert text and not text.isspace()
    assert text.count(".") == 1 and text.endswith(".")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
