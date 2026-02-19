import sys


def main() -> None:
    args = sys.argv
    print("=== Command Quest ===")

    if len(args) == 1:
        print("No arguments provided!")
        print(f"Program name: {args[0]}")
        print(f"Total arguments: {len(args)}")
        return

    print(f"Program name: {args[0]}")
    print(f"Arguments received: {len(args) - 1}")
    for i in range(1, len(args)):
        print(f"Argument {i}: {args[i]}")
    print(f"Total arguments: {len(args)}")


main()
