import sys
import math


def create_position(x: int, y: int, z: int) -> tuple:
    return tuple((x, y, z))


def calc_distance(pos1: tuple, pos2: tuple) -> float:
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return float(
        math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)
    )


def parse_coords(s: str) -> tuple:
    parts = s.split(",")
    return tuple((int(parts[0]), int(parts[1]), int(parts[2])))


def round2(val: float) -> float:
    return float(int(val * 100 + 0.5) / 100)


def main() -> None:
    print("=== Game Coordinate System ===")
    origin = tuple((0, 0, 0))
    pos1 = create_position(10, 20, 5)
    print(f"Position created: {pos1}")
    dist1 = calc_distance(origin, pos1)
    print(f"Distance between {origin} and {pos1}: {round2(dist1)}")

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

    bad_str = "abc,def,ghi"
    print(f'Parsing invalid coordinates: "{bad_str}"')
    try:
        parse_coords(bad_str)
    except ValueError as e:
        print(f"Error parsing coordinates: {e}")
        print(f"Error details - Type: ValueError, Args: {e.args}")

    pos2 = parse_coords("3,4,0")
    x, y, z = pos2
    print("Unpacking demonstration:")
    print(f"Player at x={x}, y={y}, z={z}")
    print(f"Coordinates: X={x}, Y={y}, Z={z}")

    _ = sys.argv


main()
