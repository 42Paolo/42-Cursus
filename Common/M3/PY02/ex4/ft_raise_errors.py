def check_name(plant_name):
    if not plant_name:
        raise ValueError("Plant name cannot be empty")
    print(f"Plant '{plant_name}' is healthy!")


def check_water_level(water_level):
    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 0:
        raise ValueError("Water level can't be negative")
    elif 0 <= water_level < 2:
        print("The Plant need Water!")
    else:
        print("The Plant is ok! No need more water")


def check_sunlight(sunlight_hours):
    if sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} is too low (min 2)")
    elif 2 <= sunlight_hours <= 4:
        print("The plant needs more light")
    else:
        print("The plant is okay! This much of sun it's perfect")


def check_plant_health(plant_name, water_level, sunlight_hours):
    try:
        check_name(plant_name)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        check_water_level(water_level)
    except ValueError as e:
        print(f"Error: {e}")

    try:
        check_sunlight(sunlight_hours)
    except ValueError as e:
        print(f"Error: {e}")


def main():
    print("=== Garden Plant Health Checker ===")

    print("Testing good values...")
    check_plant_health("tomato", 5, 6)

    print("Testing empty plant name...")
    try:
        check_name("")
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad water level...")
    try:
        check_water_level(15)
    except ValueError as e:
        print(f"Error: {e}")

    print("Testing bad sunlight hours...")
    try:
        check_sunlight(0)
    except ValueError as e:
        print(f"Error: {e}")

    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
