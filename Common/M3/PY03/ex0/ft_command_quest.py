import sys

if __name__ == "__main__":
    print("=== Command Quest ===")
    
    program_name = sys.argv[0]
    arguments = [int(x) for x in sys.argv[1:]]
    num_args = len(arguments)

    if num_args == 0:
        print("No arguments provided!")
    else:
        print(f"Arguments received: {num_args}")

    print(f"Program name: {program_name}")

    for i, arg in enumerate(arguments, start=1):
        print(f"Argument {i}: {arg}")

    print(f"Total elements in sys.argv: {len(sys.argv)}")
