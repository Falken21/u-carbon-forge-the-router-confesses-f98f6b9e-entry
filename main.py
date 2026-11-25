"""The Router Confesses — a make.fun entry in the router's own voice.
This program writes the router's one-line excuse for dropping a
movie-climax connection to /output/entry.txt, as a single confession.
The joke works because the router lives inside the house and has
carried everything through its walls for years, so the famous
climax line — the call is coming from inside the house — frightens it personally.
"""

import os

TEXT = "Sorry, I panicked — for three years I've carried your whole life through these walls without blinking, then the detective whispered: 'The call is coming from inside the house.'"


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(TEXT)


if __name__ == "__main__":
    main()
