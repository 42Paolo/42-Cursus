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
	day = 1
	p1 = Plant("Rose", 25, 30)
	print(f"=== Day {day} ===")
	p1.get_info()
	initial_height = p1.height_cm
	for i in range(1, 7):
		day = day + 1
		p1.age()
	print(f"=== Day {day} ===")
	p1.get_info()
	print(f"Growth this week: +{p1.height_cm - initial_height}")
