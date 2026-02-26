def main() -> None:
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        f = open("ancient_fragment.txt", "r")
        content = f.read()
        f.close()
        print("Connection established...\n")
        print("RECOVERED DATA:")
        print(content)
        print("Data recovery complete. Storage unit disconnected.")
    except FileNotFoundError:
        print("ERROR: Storage vault not found. Run data generator first.")


main()
