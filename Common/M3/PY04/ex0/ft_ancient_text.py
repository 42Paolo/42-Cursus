

def main():
    print("=== CYBER ARCHIVES - DATA RECOVERY SYSTEM ===\n")
    print("Accessing Storage Vault: ancient_fragment.txt")
    try:
        with open("ancient_fragment.txt", "r") as f:
            content = f.read()
            print("Connection established...\n")
            print("RECOVERED DATA:")
            print(f"{content}\n")
            f.close()
            print("Data recovery complete. Storage unit disconnected.")
    except (FileNotFoundError,
            PermissionError,
            IsADirectoryError,
            NotADirectoryError,
            OSError) as e:
        print("Connection not established, reason:", e)
        print("Data recovery not worked. Storage unit disconnected.\n")


if __name__ == "__main__":
    main()
