def ft_garden_summary() -> None:
    garden_name = input("Enter garden name: ")
    garden_number_plants = input("Enter number of plants: ")
    try:
        garden_number_plants = int(garden_number_plants)
        if garden_number_plants < 0:
            print("Number of plants can't be negative.")
            return
    except ValueError:
        print("Invalid input! Please enter an integer number for plants.")
        return
    print(f"Garden: {garden_name}")
    print(f"Plants: {garden_number_plants}")
    print("Status: Growing well!")