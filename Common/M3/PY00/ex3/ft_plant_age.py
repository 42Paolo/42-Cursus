def ft_plant_age() -> None::
	try:
		age_in_days = int(input("Enter plant age in days: "))
		if age_in_days < 0:
			print("Plant age in days can't be negative")
			return	
		elif age_in_days > 60:
			print("Plant is ready to harvest!")
		else:
			print("Plant needs more time to grow.")
	except ValueError:
		print("Invalid input! Please enter an integer number.")