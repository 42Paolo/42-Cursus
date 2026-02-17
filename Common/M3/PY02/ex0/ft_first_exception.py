


from ast import Return


def check_temperature(temp_str):
	try:
		print(f"Testing temperature: {temp_str}")
		temp = int(temp_str)
		if 0 <= temp <= 40:
			print(f"Temperature {temp}°C is perfect for plants!")
		elif temp < 0:
			print(f"Error: {temp}°C is too cold for plants! (min 0°C)")
		elif temp > 0:
			print(f"Error: {temp}°C is too hot for plants! (max 40°C)")
	except ValueError:
		print(f"Error '{temp_str}' is not a valid number")
	print()

def main():
	print("=== Garden Temperature Checker ===\n")

	val = [25, "abc", 100, -50]

	for v in val:
		check_temperature(v)
	
	print("All tests completed - program didn't crash!")

if __name__ == "__main__":
	main()

