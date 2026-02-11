def test_value_error() -> None:
    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}")


def test_zero_division_error() -> None:
    print("Testing ZeroDivisionError...")
    try:
        result = 10 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")


def test_file_not_found_error() -> None:
    print("Testing FileNotFoundError...")
    try:
        open("missing.txt", "r")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file 'missing.txt'")


def test_key_error() -> None:
    print("Testing KeyError...")
    try:
        plants = {"tomato": "red", "lettuce": "green"}
        color = plants["missing_plant"]
    except KeyError as e:
        print(f"Caught KeyError: {e}")


def test_multiple_errors() -> None:
    print("Testing multiple errors together...")
    
    error_operations = [
        lambda: int("xyz"),
        lambda: 5 / 0,
        lambda: open("nonexistent.txt", "r"),
    ]
    
    for operation in error_operations:
        try:
            operation()
        except (ValueError, ZeroDivisionError, FileNotFoundError):
            print("Caught an error, but program continues!")


def test_error_types() -> None:
    print("=== Garden Error Types Demo ===")
    test_value_error()
    test_zero_division_error()
    test_file_not_found_error()
    test_key_error()
    test_multiple_errors()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
