class Plant:
    """Base plant class with common features."""

    def __init__(self, name: str, height_cm: int):
        self.name = name
        self.height_cm = height_cm

    def grow(self) -> None:
        """Increase plant height by 1cm."""
        self.height_cm += 1
        print(f"{self.name} grew 1cm")

    def get_info(self) -> str:
        """Return plant information."""
        return f"{self.name}: {self.height_cm}cm"

    @staticmethod
    def validate_height(height: int) -> bool:
        """Utility function to validate height values."""
        return height >= 0


class FloweringPlant(Plant):
    """Plant that can produce flowers."""

    def __init__(self, name: str, height_cm: int, flower_color: str):
        super().__init__(name, height_cm)
        self.flower_color = flower_color
        self.is_blooming = True

    def get_info(self) -> str:
        """Return flowering plant information."""
        bloom_status = "blooming" if self.is_blooming else "not blooming"
        return f"{self.name}: {self.height_cm}cm, {self.flower_color} flowers ({bloom_status})"


class PrizeFlower(FloweringPlant):
    """Special flowering plant with prize points."""

    def __init__(self, name: str, height_cm: int, flower_color: str, prize_points: int):
        super().__init__(name, height_cm, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> str:
        """Return prize flower information."""
        return f"{super().get_info()}, Prize points: {self.prize_points}"


class GardenManager:
    """Manager for handling multiple gardens with nested statistics."""

    total_gardens = 0

    class GardenStats:
        """Nested helper class for calculating garden statistics."""

        def __init__(self):
            self.plants_added = 0
            self.total_growth = 0
            self.regular_plants = 0
            self.flowering_plants = 0
            self.prize_flowers = 0

        def add_plant(self, plant: Plant) -> None:
            """Track a new plant addition."""
            self.plants_added += 1
            if isinstance(plant, PrizeFlower):
                self.prize_flowers += 1
            elif isinstance(plant, FloweringPlant):
                self.flowering_plants += 1
            else:
                self.regular_plants += 1

        def record_growth(self) -> None:
            """Record growth event."""
            self.total_growth += 1

        def get_summary(self) -> str:
            """Get statistics summary."""
            return (f"Plants added: {self.plants_added}, "
                    f"Total growth: {self.total_growth}cm\n"
                    f"Plant types: {self.regular_plants} regular, "
                    f"{self.flowering_plants} flowering, "
                    f"{self.prize_flowers} prize flowers")

    def __init__(self, owner_name: str):
        self.owner_name = owner_name
        self.plants = []
        self.stats = GardenManager.GardenStats()
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant to the garden."""
        self.plants.append(plant)
        self.stats.add_plant(plant)
        print(f"Added {plant.name} to {self.owner_name}'s garden")

    def grow_all(self) -> None:
        """Make all plants grow."""
        print(f"{self.owner_name} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.stats.record_growth()

    def get_total_score(self) -> int:
        """Calculate total garden score based on plant heights."""
        return sum(plant.height_cm for plant in self.plants)

    def print_report(self) -> None:
        """Print comprehensive garden report."""
        print(f"\n=== {self.owner_name}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.get_info()}")
        print(self.stats.get_summary())

    @classmethod
    def create_garden_network(cls, owner_names: list) -> list:
        """Class method to create multiple gardens at once."""
        return [cls(name) for name in owner_names]

    @classmethod
    def get_total_gardens(cls) -> int:
        """Get total number of gardens managed."""
        return cls.total_gardens


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    # Create gardens
    alice_garden = GardenManager("Alice")
    bob_garden = GardenManager("Bob")

    # Create plants
    oak = Plant("Oak Tree", 100)
    rose = FloweringPlant("Rose", 25, "red")
    sunflower = PrizeFlower("Sunflower", 50, "yellow", 10)

    # Add plants to Alice's garden
    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    # Add plants to Bob's garden
    bob_garden.add_plant(Plant("Fern", 30))
    bob_garden.add_plant(FloweringPlant("Daisy", 20, "white"))

    # Grow all plants in Alice's garden
    alice_garden.grow_all()

    # Print Alice's garden report
    alice_garden.print_report()

    # Test static method
    print(f"Height validation test: {Plant.validate_height(100)}")

    # Compare garden scores
    print(f"Garden scores - Alice: {alice_garden.get_total_score()}, "
          f"Bob: {bob_garden.get_total_score()}")

    # Display total gardens managed
    print(f"Total gardens managed: {GardenManager.get_total_gardens()}")
