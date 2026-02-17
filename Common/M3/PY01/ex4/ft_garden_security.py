class Plant:
	def __init__(self, name, height_cm, age_d):
		self.name = name
		self._height_cm = height_cm
		self._age_d = age_d

	@property
	def height_cm(self):
		return self._height_cm

	@height_cm.setter
	def height_cm(self, new_height):
		if new_height <= 0:
			raise ValueError(f"Invalid operation attempted: height {new_height} [REJECTED]\nSecurity: Negative height rejected")
		else:
			self._height_cm = new_height
			print(f"Height updated: {self._height_cm}cm [OK]")

	@property
	def age_d(self):
		return self._age_d

	@age_d.setter
	def age_d(self, new_age):
		if new_age < 0:
			raise ValueError(f"Invalid operation attempted: age {new_age} [REJECTED]\nSecurity: Negative age rejected")
		else:
			self._age_d = new_age
			print(f"Age updated: {self._age_d} days [OK]")

	def print_info(self):
		print(f"{self.name} ({self._height_cm}cm, {self._age_d} days)")


def main():
    p1 = Plant("Rose", 25, 30)
    p2 = Plant("Tulipano", 40, 10)
    p3 = Plant("Eocalipto", 40, 15)

    plants = [p1, p2, p3]

    print("=== Garden Security System ===")
    
    for p in plants:
        print(f"Plant created: {p.name}")
        p.height_cm = p.height_cm
        p.age_d = p.age_d

    print()

    try:
        p1.height_cm = -5
    except ValueError as e:
        print(e)

    print(f"\nCurrent plant: {p1.name} ({p1.height_cm}cm, {p1.age_d} days)")

if __name__ == "__main__":
	main()