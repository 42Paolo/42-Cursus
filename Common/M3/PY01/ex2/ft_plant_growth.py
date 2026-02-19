class Plant:
    def __init__(self, name, height_cm, age_d):
        self.name = name
        self.height_cm = height_cm
        self.age_d = age_d
        self.height_start = height_cm

    def age(self):
        self.age_d += 1

    def grow(self):
        self.height_cm += 1
        self.age()

    def get_info(self):
        print(f"{self.name}: {self.height_cm}cm {self.age_d} days old")

    def life(self):
        if 0 <= self.age_d <= 30:
            print(f"Pianta {self.name}: Giovane")
        elif 31 <= self.age_d <= 200:
            print(f"Pianta {self.name}: Adulta")
        elif 201 <= self.age_d <= 365:
            print(f"Pianta {self.name}: Vecchia")
        elif self.age_d > 365:
            print(f"Pianta {self.name}: Morta")


def grow_plant(p: Plant):
    print("=== Day 1 ===")
    p.grow()
    p.get_info()
    for i in range(2, 7):
        p.grow()
    print("=== Day 7 ===")
    p.get_info()
    print(f"Growth this week: +{p.height_cm - p.height_start}")


def main():
    plants = [
        Plant("Rose", 44, 5),
        Plant("Tulipano", 10, 10),
        Plant("Eocalipto", 20, 15)
    ]
    for p in plants:
        grow_plant(p)
        p.life()
        print()


if __name__ == "__main__":
    main()
