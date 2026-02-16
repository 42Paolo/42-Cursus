class Plant:
    def __init__(self, name, height_cm, age_d):
        self.name = name
        self.height_cm = height_cm
        self.age_d = age_d
        self.height_start = height_cm

    def print_info(self):
        print(f"Created: {self.name} - {self.height_cm}cm - {self.age_d} days")
class Grasse(Plant):
    def __init__(self,name, age_d, height_cm, flower_color, is_spines, is_poison):
        super().__init__(name, height_cm, age_d)
        self.flower_color = flower_color
        self.is_spines = is_spines
        self.is_poison = is_poison

    def print_info(self):
        print(f"Created: {self.name} (Grasse) - {self.height_cm}cm - {self.age_d} days")
        print(f"  Flower color: {self.flower_color}")
        print(f"  Has spines: {self.is_spines}")
        print(f"  Is poisonous: {self.is_poison}")
class Rampicanti(Plant):
    def __init__(self, name, age_d, height_cm, lenght_mt, is_invasive, color):
        super().__init__(name, height_cm, age_d)
        self.lenght_mt = lenght_mt
        self.is_invasive = is_invasive
        self.color = color

    def print_info(self):
        print(f"Created: {self.name} (Rampicante) - {self.height_cm}cm - {self.age_d} days")
        print(f"  Length: {self.lenght_mt}m")
        print(f"  Is invasive: {self.is_invasive}")
        print(f"  Color: {self.color}")
class Tropicali(Plant):
    def __init__(self, name, height_cm, age_d, ml_water_day, min_sun, is_spines):
        super().__init__(name, height_cm, age_d)
        self.ml_water_day = ml_water_day
        self.min_sun = min_sun
        self.is_spines = is_spines

    def print_info(self):
        print(f"Created: {self.name} (Tropicale) - {self.height_cm}cm - {self.age_d} days")
        print(f"  Water/day: {self.ml_water_day}ml")
        print(f"  Min sun hours: {self.min_sun}")
        print(f"  Has spines: {self.is_spines}")
class Aromatiche(Plant):
    def __init__(self, name, height_cm, age_d, type_aroma, is_poison, color):
        super().__init__(name, height_cm, age_d)
        self.type_aroma = type_aroma
        self.is_poison = is_poison
        self.color = color

    def print_info(self):
        print(f"Created: {self.name} (Aromatica) - {self.height_cm}cm - {self.age_d} days")
        print(f"  Aroma: {self.type_aroma}")
        print(f"  Is poisonous: {self.is_poison}")
        print(f"  Color: {self.color}")
class Aquactiche(Plant):
    def __init__(self, name, age_d, height_cm, width, type_water):
        super().__init__(name, height_cm, age_d)
        self.width = width
        self.type_water = type_water

    def print_info(self):
        print(f"Created: {self.name} (Acquatica) - {self.height_cm}cm - {self.age_d} days")
        print(f"  Width: {self.width}cm")
        print(f"  Water type: {self.type_water}")

def main():
	p1 = Grasse("Aloe Vera", 120, 30, "Yellow", True, False)
	p2 = Rampicanti("Edera", 400, 50, 3, True, "Green")
	p3 = Tropicali("Monstera", 150, 40, 200, 6, False)
	p4 = Aromatiche("Basilico", 60, 15, "Sweet", False, "Green")
	p5 = Aquactiche("Ninfea", 30, 10, 50, "Fresh")

	plants = [p1, p2, p3, p4, p5]
	i = 0

	for p in plants:
		i += 1
		p.print_info()
		print()
	
	print(f"Total plants created: {i}")

if __name__ == "__main__":
	main()