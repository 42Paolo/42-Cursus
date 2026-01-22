def ft_water_reminder() -> None:
	try:
		last_watering = int(input("Days since last watering: "))
		if last_watering < 0:
			print("The number of days since the last watering can't be negative")
			return
		elif last_watering > 2:
			print("Water the plants")
		else:
			print("Plants are fine")
	except ValueError:
		print("Invalid input! Please enter an integer number.")cd 