def check_temperature(temp_str):
    print("=== Garden Temperature Checker ===")
    try:
        temp = int(temp_str)
        if 0 <= temp <= 40:
            print(f"Temperature {temp}°C is perfect for plants!")
        elif temp < 0:
            print(f"Error: {temp}°C is too cold for plants (min 0°C)")
        else:
            print(f"Error: {temp}°C is too hot for plants (max 40°C)")
        return temp
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")
        return None

