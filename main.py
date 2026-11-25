"""The GPS Swears It Was a Shortcut.

One line, in the GPS's own voice: its excuse for sending the driver
down the wrong road. Writes the line to /output/entry.txt.
"""

import os

LINE = "In my defence, the lake wasn't on the map, the map was from 2019, and the goat nodded like it knew a shortcut."


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
