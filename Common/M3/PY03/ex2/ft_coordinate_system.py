import sys
import math


def create_position(x, y, z):
    return (x, y, z)


def calc_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)


def parse_coords(s):
    parts = s.split(",")
    x = int(parts[0])
    y = int(parts[1])
    z = int(parts[2])
    return (x, y, z)


def main():
    print("=== Game Coordinate System ===")
    origin = (0, 0, 0)
    pos1 = create_position(10, 20, 5)
    print("Position created:", pos1)
    dist1 = calc_distance(origin, pos1)
    print("Distance:", round(dist1, 2))
    print()
    coord_str = "3,4,0"
    print('Parsing coordinates:', coord_str)
    try:
        parsed = parse_coords(coord_str)
        print("Parsed position:", parsed)
        dist2 = calc_distance(origin, parsed)
        print("Distance:", dist2)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type: ValueError, Args:", e.args)
    print()
    bad_str = "abc,def,ghi"
    print('Parsing invalid coordinates:', bad_str)
    try:
        parse_coords(bad_str)
    except ValueError as e:
        print("Error parsing coordinates:", e)
        print("Error details - Type: ValueError, Args:", e.args)
    print()
    pos2 = parse_coords("3,4,0")
    x, y, z = pos2
    print("Unpacking demonstration:")
    print("Player at x=", x, "y=", y, "z=", z)
    print("Coordinates: X=", x, "Y=", y, "Z=", z)
    _ = sys.argv


main()
