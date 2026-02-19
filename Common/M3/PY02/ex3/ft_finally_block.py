class Vegetable:
    def __init__(self, name):
        self.name = name


def water_plants(plant_list):
    print("Opening watering system")

    try:
        for v in plant_list:
            print(f"Watering {v.name}")

    except AttributeError:
        print("Error: Cannot water None - invalid plant!")

    finally:
        print("Closing watering system (cleanup)")


def main():
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")

    v1 = Vegetable("tomato")
    v2 = Vegetable("lettuce")
    v3 = Vegetable("carrots")

    vegetables = [v1, v2, v3]
    water_plants(vegetables)
    print("Watering completed successfully!\n")

    print("Testing with error...")

    v4 = Vegetable("tomato")
    vegetables_with_error = [v4, None]

    water_plants(vegetables_with_error)
    print("Cleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
