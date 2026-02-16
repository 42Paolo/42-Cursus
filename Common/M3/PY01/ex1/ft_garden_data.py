class Plant:
	def __init__(self, name, height_cm, age_d):
		self.name = name
		self.height_cm = height_cm
		self.age_d = age_d
		
	def print_info(self):
		print(f"Plant: {self.name}\nHeight: {self.height_cm}cm\nAge: {self.age_d}\n")

def main(): 
	plants = [
		Plant("Rose", 25, 30),
		Plant("Tulipano", 40, 10),
		Plant("Eocalipto", 40, 15)
	]
	
	print("=== Garden Plant Registry ===")
	for p in plants:
		p.print_info()

	print("=== End of Program ===")


if __name__ == "__main__":
	main()