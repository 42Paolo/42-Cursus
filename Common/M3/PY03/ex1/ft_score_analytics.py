from ast import arguments
import sys

if __name__ == "__main__":
	print("=== Player Score Analytics ===")
	arguments = [int(x) for x in sys.argv[1:]]
	arg_len = len(arguments)
	if arg_len == 0:
		print("No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...")
	else:
		print(f"Total players: {arg_len}")
		print(f"Total score: {sum(arguments)}")
		print(f"Average score: {sum(arguments)/arg_len}")
		print(f"High score: {max(arguments)}")
		print(f"Low score: {min(arguments)}")
		print(f"Score range: {max(arguments) - min(arguments)}")