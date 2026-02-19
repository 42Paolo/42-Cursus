import sys



def main() -> None:
	args = sys.argv
	print("=== Command Quest ===")
	if len(args) == 1:
		print("No arguments provided!")
		print(f"Program name: {args[0]}")
		print(f"Total arguments: {len(args)}")
	else:
		print(f"Program name: {args[0]}")
		print(f"Arguments received: {len(args) - 1}")
		for i, arg in enumerate(args[1:], 1):
			print(f"Argument {i}: {arg}")
		print(f"Total arguments: {len(args)}")


main()
