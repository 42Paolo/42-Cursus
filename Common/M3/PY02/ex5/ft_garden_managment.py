class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plants = {}
        self.water_tank = 100

    def add_plant(self, name, water_level, sunlight_hours):
        if not name:
            raise PlantError("Plant name cannot be empty!")

        if water_level < 1 or water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")

        if sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} invalid")

        self.plants[name] = {
            "water_level": water_level,
            "sunlight_hours": sunlight_hours
        }
        print(f"Added {name} successfully")

    def water_plants(self):
        print("Opening watering system")

        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")

        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self, name):
        if name not in self.plants:
            raise PlantError(f"Plant {name} not found")

        plant = self.plants[name]
        water = plant["water_level"]
        sun = plant["sunlight_hours"]

        if water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")

        print(f"{name}: healthy (water: {water}, sun: {sun})")

    def use_water(self, amount):
        if self.water_tank < amount:
            raise WaterError("Not enough water in tank")
        self.water_tank -= amount


def test_garden_management():
    print("=== Garden Management System ===")

    manager = GardenManager()

    print("\nAdding plants to garden...")
    try:
        manager.add_plant("tomato", 5, 8)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("lettuce", 6, 7)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")

    try:
        manager.add_plant("", 5, 8)
    except (PlantError, ValueError) as e:
        print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    manager.water_plants()

    print("\nChecking plant health...")
    try:
        manager.check_plant_health("tomato")
    except (PlantError, ValueError) as e:
        print(f"Error checking tomato: {e}")

    manager.plants["lettuce"]["water_level"] = 15

    try:
        manager.check_plant_health("lettuce")
    except (PlantError, ValueError) as e:
        print(f"Error checking lettuce: {e}")

    print("\nTesting error recovery...")
    try:
        manager.use_water(200)
    except GardenError as e:
        print(f"Caught GardenError: {e}")

    print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
