def ft_plot_area():
    try:
        width = int(input("Enter width: "))
        lenght = int(input("Enter lenght: "))
        if width <= 0 or lenght <= 0:
            print("Width and length must be positive numbers.")
            return
        plot_area = width * lenght
        print(f"Plot area: {plot_area}")
    except ValueError:
        print("Invalid input! Please enter an integer number.")