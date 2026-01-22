def ft_count_harvest_iterative() -> None:
	try:
		days_left = int(input("Days until harvest: "))
		if days_left < 0:
			print("Days left can't be negative")
			return
		i = 1
		while i <= days_left:
			print(f"Day {i}")
			i += 1
		print("Harvest time!")
	except ValueError:
		print("Invalid input! Please enter an integer number.")