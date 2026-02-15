"""Module for managing and calculating distances in a 3D game
coordinate system."""


import math


def main() -> None:
    """
    Handle 3D coordinate creation, parsing, and distance calculations.

    Demonstrates coordinate unpacking, distance from origin using Euclidean
    norm, and error handling for malformed input strings.
    """
    print("=== Game Coordinate System ===\n")

    pos_init = (0, 0, 0)

    pos = (10, 20, 5)
    distance = math.sqrt(sum((a - b)**2 for a, b in zip(pos, pos_init)))
    print(f"Position created: {pos}")
    print(f"Distance between {pos_init} and {pos}: {distance:.2f}\n")

    raw_pos: str = "3, 4, 0"
    t_pos = tuple(int(n) for n in raw_pos.split(","))
    distance = math.sqrt(sum((a - b)**2 for a, b in zip(t_pos, pos_init)))
    print(f'Parsing coordinates: "{raw_pos}"')
    print(f"Parsed position: {t_pos}")
    print(f"Distance between {pos_init} and {t_pos}: {distance:.2f}\n")

    invalid_pos: str = "abc, def, ghi"
    char_pos: list[int] = []
    print(f'Parsing invalid coordinates: "{invalid_pos}"')
    try:
        for pos in invalid_pos.split(","):
            char_pos += [int(pos)]
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: {type(e).__name__}, Args: {e.args}\n")

    print("Unpacking demonstration:")
    x, y, z = t_pos
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


if __name__ == "__main__":
    main()
