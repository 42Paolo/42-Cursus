def ft_plot_area() -> None:
	try:
		width = int(input("Enter width: "))
		length = int(input("Enter length: "))
		if width <= 0 or length <= 0:
			print("Width and length must be positive numbers.")
			return
		plot_area = width * length
		print(f"Plot area: {plot_area}")
	except ValueError:
		print("Invalid input! Please enter an integer number.")