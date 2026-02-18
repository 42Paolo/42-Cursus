import sys

def ft_len(obj):
	count = 0
	for _ in obj:
		count += 1
	return count

def main():
	print("=== Command Quest ===")
	argc = ft_len(sys.argv)
	if argc == 1:
		print("No arguments provided!")
	print(f"Program name: {sys.argv[0]}")		
	if argc != 1:
		print(f"Arguments received: {argc-1}")
		for i in range(1, argc):
			print(f"Argument {i}: {sys.argv[i]}")
	print(f"Total arguments: {argc}")

if __name__ == "__main__":
	main()