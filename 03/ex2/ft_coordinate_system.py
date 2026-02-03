"""Docstrings"""

import sys
import math

def main() -> None:
    print("=== Game Coordinate System ===\n")

    pos = (10, 20, 5)
    distance = math.sqrt(sum(n**2 for n in pos))
    print(f"Position created: {pos}")
    print(f"Distance between (0, 0, 0) and {pos}: {distance:.2f}\n")

    raw_pos = "3, 4, 0"
    int_pos = []
    print(f'Parsing coordinates: "{raw_pos}"')
    for pos in raw_pos.split(","):
        int_pos += [int(pos)]
    int_distance = math.sqrt(sum(n**2 for n in int_pos))
    t_pos = tuple(int_pos)
    print(f"Parsed options: {t_pos}")  
    print(f"Distance between (0, 0, 0) and {t_pos}: {int_distance}\n")

    invalid_pos = "abc, def, ghi"
    char_pos = []
    print(f'Parsing invalid coordinates: "{invalid_pos}"')
    try:
        for pos in invalid_pos.split(","):
            char_pos += [int(pos)]
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error detail - Type: {type(e).__name__}, Args: {e.args}\n")

    print(f"Unpacking demonstration:")
    x, y, z = t_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
