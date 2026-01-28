class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def grow(self):
        self.height_cm += 1

    def age(self):
        self.age_days += 1
        self.grow()

    def get_info(self):
        print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    print("=== Plant Factory Output ===")
    plants = []
    for name, height, age in plants_data:
        plant = Plant(name, height, age)
        plants.append(plant)
        print(f"Created: {name} ({height}cm, {age} days)")
    print(f"Total plants created: {len(plants)}")
