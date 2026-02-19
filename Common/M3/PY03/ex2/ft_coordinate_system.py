import sys
import math


def create_position(x: int, y: int, z: int) -> tuple[int, int, int]:
    return (x, y, z)


def calc_distance(
    pos1: tuple[int, int, int],
    pos2: tuple[int, int, int]
) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coords(coord_str: str) -> tuple[int, int, int]:
    parts = coord_str.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main() -> None:
    print("=== Game Coordinate System ===")

    origin: tuple[int, int, int] = (0, 0, 0)

    pos1 = create_position(10, 20, 5)
    print(f"Position created: {pos1}")
    dist1 = calc_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round(dist1, 2)}")

    print()
    coord_str = "3,4,0"
    print(f'Parsing coordinates: "{coord_str}"')
    try:
        parsed = parse_coords(coord_str)
        print(f"Parsed position: {parsed}")
        dist2 = calc_distance(origin, parsed)
        print(f"Distance between {origin} and {parsed}: {dist2}")
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print()
    bad_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_str}"')
    try:
        parse_coords(bad_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    print()
    coord_str2 = "3,4,0"
    pos2 = parse_coords(coord_str2)
    x, y, z = pos2
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

    _ = sys.argv


main()
