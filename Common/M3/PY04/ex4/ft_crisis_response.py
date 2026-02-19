
def main():
    print("=== CYBER ARCHIVES - CRISIS RESPONSE SYSTEM ===")
    try:
        print("CRISIS ALERT: Attempting access to 'lost_archive.txt'...")
        with open("lost_archive.txt", "r") as file:
            data = file.read()
    except FileNotFoundError:
        print("RESPONSE: Archive not found in storage matrix")
    finally:
        print("STATUS: Crisis handled, system stable")

    try:
        print("\nCRISIS ALERT: Attempting access to 'classified_vault.txt'...")
        with open("classified_vault.txt", "r") as file:
            _ = file.read()
    except PermissionError:
        print("RESPONSE: Security protocols deny access")
    finally:
        print("STATUS: Crisis handled, security maintained")

    try:
        print(
            "\nROUTINE ACCESS: Attempting access to 'standard_archive.txt'..."
            )
        with open("standard_archive.txt", "r") as file:
            data = file.read()
            print(f"SUCCESS: Archive recovered - ''{data}''")
    except Exception as e:
        print(f"[ERROR] : {e}")
    finally:
        print("STATUS: Normal operations resumed")

    print("\nAll crisis scenarios handled successfully. Archives secure.")


if __name__ == "__main__":
    main()
