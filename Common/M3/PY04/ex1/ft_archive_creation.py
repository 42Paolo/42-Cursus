

def main():
    print("=== CYBER ARCHIVES - PRESERVATION SYSTEM ===")
    try:
        print("Initializing new storage unit: new_discovery.txt")
        with open("new_discovery.txt", "a") as f:
            print("Storage unit created successfully...\n")
            print("Inscribing preservation data...")
            print("[ENTRY 001] New quantum algorithm discovered")
            print("[ENTRY 002] Efficiency increased by 347%")
            print("[ENTRY 003] Archived by Data Archivist trainee")
            f.write("[ENTRY 001] New quantum algorithm discovered")
            f.write("[ENTRY 002] Efficiency increased by 347%")
            f.write("[ENTRY 003] Archived by Data Archivist trainee")
            print("\nData inscription complete. Storage unit sealed.")
            print("Archive 'new_discovery.txt' ready for "
                  "long-term preservation.")
    except (FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            NotADirectoryError,
            OSError) as e:
        print("\nData inscription not started. Storage unit not sealed.")
        print(f"Archive 'new_discovery.txt' not created, reason: {e}")


if __name__ == "__main__":
    main()
