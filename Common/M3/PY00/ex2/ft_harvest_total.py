def ft_harvest_total() -> None::
	try:
		d1 = int(input("Day 1 harvest: "))
		d2 = int(input("Day 2 harvest: "))
		d3 = int(input("Day 3 harvest: "))
		if d1 < 0 or d2 < 0 or d3 < 0:
			print("Harvest can't be negative")
			return
		print(f"Total harvest: {d1 + d2 + d3}")
	except ValueError:
		 print("Invalid input! Please enter an integer number.")
