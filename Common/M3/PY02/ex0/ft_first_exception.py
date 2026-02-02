def check_temperature(temp_str: str) -> float:
    try:
        temp = int(temp_str)
        if temp < 0:
            raise ValueError(f"{temp}°C is too cold for plants (min 0°C)")
        if temp > 40:
            raise ValueError(f"{temp}°C is too hot for plants (max 40°C)")
        return temp
    except ValueError as e:
        if "invalid literal" in str(e):
            raise ValueError(f"'{temp_str}' is not a valid number")
        raise


def test_temperature_input() -> None:
    print("=== Garden Temperature Checker ===")
    
    test_cases = ["25", "abc", "100", "-50"]
    
    for temp_str in test_cases:
        print(f"Testing temperature: {temp_str}")
        try:
            temp = check_temperature(temp_str)
            print(f"Temperature {temp}°C is perfect for plants!")
        except ValueError as e:
            print(f"Error: {e}")
    
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    test_temperature_input()
