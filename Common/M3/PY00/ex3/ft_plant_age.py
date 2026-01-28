def ft_plant_age():
    age_in_days = int(input("Enter plant age in days: "))
    if age_in_days > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
