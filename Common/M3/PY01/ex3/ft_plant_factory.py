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
	total_plants = 0
	plants = [Plant(name, height, age) for name, height, age in plants_data]
	for p in plants:
		p.get_info()
		total_plants = total_plants + 1
	print(f"\nTotal Plants created: {total_plants}")
	