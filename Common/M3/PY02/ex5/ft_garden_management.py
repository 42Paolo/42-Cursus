from typing import Dict, List


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


    def add_plant(self, name: str, water_level: int = 5, sunlight_hours: int = 8) -> None:
        if not name or name.strip() == "":
            raise ValueError("Plant name cannot be empty!")
        
        self.plants[name] = {
            "water": water_level,
            "sunlight": sunlight_hours
        }
        print(f"Added {name} successfully")
    
    def water_plants(self) -> None:
        print("Opening watering system")
        try:
            for plant_name in self.plants:
                print(f"Watering {plant_name} - success")
        finally:
            print("Closing watering system (cleanup)")
    
    def check_plant_health(self, name: str) -> None:
        if name not in self.plants:
            raise PlantError(f"Plant '{name}' not found in garden")
        
        plant = self.plants[name]
        water = plant["water"]
        sun = plant["sunlight"]
        
        if water < 1 or water > 10:
            raise ValueError(f"Water level {water} is too high (max 10)")
        if sun < 2 or sun > 12:
            raise ValueError(f"Sunlight hours {sun} is invalid")
        
        print(f"{name}: healthy (water: {water}, sun: {sun})")
    
    def perform_watering_cycle(self, has_water: bool = True) -> None:
        if not has_water:
            raise GardenError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    
    garden = GardenManager()
    
    print("Adding plants to garden...")
    try:
        garden.add_plant("tomato", 5, 8)
        garden.add_plant("lettuce", 15, 6)
        garden.add_plant("", 5, 8)
    except ValueError as e:
        print(f"Error adding plant: {e}")
    
    print("\nWatering plants...")
    garden.water_plants()
    
    print("\nChecking plant health...")
    try:
        garden.check_plant_health("tomato")
    except (ValueError, PlantError) as e:
        print(f"Error checking tomato: {e}")
    
    try:
        garden.check_plant_health("lettuce")
    except (ValueError, PlantError) as e:
        print(f"Error checking lettuce: {e}")
    
    print("\nTesting error recovery...")
    try:
        garden.perform_watering_cycle(has_water=False)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")
    
    print("\nGarden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
