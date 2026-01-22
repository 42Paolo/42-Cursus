def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if quantity < 0:
        print("The quantity of seeds can't be negative")
        return
    if unit == "packets":
        print(f"{seed_name} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_name} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_name} seeds: covers {quantity} square meters")
    else:
        print(f"{seed_name} seeds: {quantity} {unit}")
