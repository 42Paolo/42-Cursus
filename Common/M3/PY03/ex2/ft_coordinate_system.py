import sys
import math


def calculate_distance(p1: tuple, p2: tuple) -> float:
    return math.sqrt(
        (p2[0] - p1[0]) ** 2 +
        (p2[1] - p1[1]) ** 2 +
        (p2[2] - p1[2]) ** 2
    )


def parse_coords(s: str) -> tuple:
    parts = s.split(",")
    return (int(parts[0]), int(parts[1]), int(parts[2]))


def main() -> None:
    print("=== Game Coordinate System ===")

    origin = (0, 0, 0)
    pos1 = (10, 20, 5)
    print(f"Position created: {pos1}")
    d = round(calculate_distance(origin, pos1), 2)
    print(f"Distance between {origin} and {pos1}: {d}")

    print()
    print('Parsing coordinates: "3,4,0"')
    try:
        parsed = parse_coords("3,4,0")
        print(f"Parsed position: {parsed}")
        d2 = calculate_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {d2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")

    print()
    print('Parsing invalid coordinates: "abc,def,ghi"')
    try:
        parse_coords("abc,def,ghi")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print()
    print("Unpacking demonstration:")
    x, y, z = parsed
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")


main()
