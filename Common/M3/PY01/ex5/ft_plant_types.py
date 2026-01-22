class Plant:
    def __init__(self, name, height_cm, age_days):
        self.name = name
        self.height_cm = height_cm
        self.age_days = age_days

    def get_info(self):
        return f"{self.name}: {self.height_cm}cm, {self.age_days} days"

class Flower(Plant):
    def __init__(self, name, height_cm, age_days, color):
        super().__init__(name, height_cm, age_days)
        self.color = color

    def bloom(self):
        print(f"{self.name} is blooming beautifully!")

    def get_info(self):
        return f"{self.name} (Flower): {self.height_cm}cm, {self.age_days} days, {self.color} color"

class Tree(Plant):
    def __init__(self, name, height_cm, age_days, trunk_diameter):
        super().__init__(name, height_cm, age_days)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self):
        shade_area = self.trunk_diameter * self.height_cm // 10
        print(f"{self.name} provides {shade_area} square meters of shade")

    def get_info(self):
        return f"{self.name} (Tree): {self.height_cm}cm, {self.age_days} days, {self.trunk_diameter}cm diameter"

class Vegetable(Plant):
    def __init__(self, name, height_cm, age_days, harvest_season, nutritional_value):
        super().__init__(name, height_cm, age_days)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self):
        return f"{self.name} (Vegetable): {self.height_cm}cm, {self.age_days} days, {self.harvest_season} harvest"

    def nutrition_info(self):
        print(f"{self.name} is rich in {self.nutritional_value}")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")

    f1 = Flower("Margherita", 25, 30, "bianco")
	f2 = Flower("Girasole", 180, 90, "giallo")
	t1 = Tree("Olivo", 400, 3650, 70)
	t2 = Tree("Quercia", 500, 5000, 80)
	v1 = Vegetable("Pomodoro", 80, 90, "estate", "vitamina C")
	v2 = Vegetable("Carota", 40, 60, "primavera", "vitamina A")
	
    plants = [f1, f2, t1, t2, v1, v2]

    for plant in plants:
        print(plant.get_info())
        if isinstance(plant, Flower):
            plant.bloom()
        elif isinstance(plant, Tree):
            plant.produce_shade()
        elif isinstance(plant, Vegetable):
            plant.nutrition_info()