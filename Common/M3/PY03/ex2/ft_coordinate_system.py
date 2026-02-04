import math
import sys

def dist_cord(p1: tuple, p2: tuple) -> float:
    x1, y1, z1 = p1
    x2, y2, z2 = p2
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)

def parsing_co(str_cord: str) -> tuple:
    parts = str_cord.split(',')
    return (int(parts[0]), int(parts[1]), int(parts[2]))

def main() -> None:
    spawn_co = (0, 0, 0)
    
    if len(sys.argv) > 1:
        raw_input = sys.argv[1]
    else:
        raw_input = "10,20,5"

    try:
        target_pos = parsing_co(raw_input)
        dist = dist_cord(spawn_co, target_pos)
        
        print(f"Position: {target_pos}")
        print(f"Distance: {dist:.2f}")
        
        x, y, z = target_pos
        print(f"X={x}, Y={y}, Z={z}")
        
    except (ValueError, IndexError) as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()