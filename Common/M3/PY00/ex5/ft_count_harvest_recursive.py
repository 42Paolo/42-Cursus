def ft_count_harvest_recursive(day=1, days_left=None):
    if days_left is None:
        days_left = int(input("Days until harvest: "))
    if day > days_left:
        print("Harvest time!")
        return
    print(f"Day {day}")
    ft_count_harvest_recursive(day + 1, days_left)
