def ft_count_harvest_recursive(day=1, days_left=None) -> None:
    if days_left is None:
        try:
            days_left = int(input("Days until harvest: "))
            if days_left < 0:
                print("Days left can't be negative")
                return
        except ValueError:
            print("Invalid input! Please enter an integer number.")
            return
    if day > days_left:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1, days_left)