class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        print(f"Plant created: {self.name}")
        self.set_height(height_cm)
        self.set_age(age_days)
    
    def set_height(self, height_cm):
        if height_cm < 0:
            print(f"Invalid operation attempted: height {height_cm}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.height_cm = height_cm
            print(f"Height updated: {height_cm}cm [OK]")

    def set_age(self, age_days):
        if age_days < 0:
            print(f"Invalid operation attempted: age {age_days} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.age_days = age_days
            print(f"Age updated: {age_days} days [OK]")

    def get_height(self):
        return self.height_cm
    
    def get_age(self):
        return self.age_days
    
    def get_info(self):
        print(f"Current plant: {self.name} ({self.height_cm}cm, {self.age_days} days)")

if __name__ == "__main__":
    plants_data = [
        ("Rose", 25, 30),
        ("Oak", 200, 365),
        ("Cactus", 5, 90),
        ("Sunflower", 80, 45),
        ("Fern", 15, 120)
    ]
    plants = [Plant(name, height, age) for name, height, age in plants_data]
    print("\n=== Testing security ===")
    plants[0].set_height(-20)
    plants[0].get_info()