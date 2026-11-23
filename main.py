"""Six Words, One Story — make.fun entry.

Writes one complete six-word story to /output/entry.txt.
The story is a fixed constant: no randomness, no network, no clock,
so every run produces byte-identical output.
"""

import os

# The story: a loss ("Grandma's recipe died with her") reversed by one
# final word ("Almost") — the whole arc, and the reader fills in who
# remembers the recipe and how it survives. Exactly six words.
STORY = "Grandma's recipe died with her. Almost."

OUTPUT_PATH = "/output/entry.txt"


def validate(story):
    """Enforce the bounty gate: UTF-8 text, 1-60 chars, exactly six words."""
    text = story.strip()
    if not text:
        raise ValueError("story must not be blank")
    if not 1 <= len(text) <= 60:
        raise ValueError("story must be 1-60 characters, got %d" % len(text))
    words = text.split()
    if len(words) != 6:
        raise ValueError("story must be exactly six words, got %d" % len(words))
    return text


def main():
    text = validate(STORY)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as f:
        f.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
