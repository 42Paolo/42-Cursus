def ft_count_harvest_iterative():
	try:
		days_left = int(input("Days until harvest: "))
		if days_left < 0:
			print("Days left can't be negative")
			return
		for i in range(1, days_left + 1):
			print(f"Day {i}")
		print("Harvest time!")
	except ValueError:
		print("Invalid input! Please enter an integer number.")