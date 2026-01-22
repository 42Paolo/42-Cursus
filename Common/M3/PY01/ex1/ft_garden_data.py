class Plant:
	def __init__(self, name, height_cm, age_days):
		self.name = name
		self.height_cm = height_cm
		self.age_days = age_days
	
	def print_info(self):
	    print(f"{self.name}: {self.height_cm}cm, {self.age_days} days old")


if __name__ == "__main__":
	p1 = Plant("Rose", 25, 30)
	p2 = Plant("Sunflower", 80, 45)
	p3 = Plant("Cactus", 15, 120)
	p4 = Plant("Petalo", 30, 40)
	print("=== Garden Plant Registry ===")
	p1.print_info()
	p2.print_info()
	p3.print_info()
	p4.print_info()
