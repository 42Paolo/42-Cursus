import sys


def main() -> None:
    print("=== Player Score Analytics ===")
    args = sys.argv[1:]
    if len(args) == 0:
        print("No scores provided. Usage: python3 ft_score_analytics.py"
              " <score1> <score2> ...")
        return

    scores: list[int] = []
    for arg in args:
        try:
            scores.append(int(arg))
        except ValueError:
            print(f"Invalid score ignored: {arg}")

    if len(scores) == 0:
        print("No valid scores to process.")
        return

    total = sum(scores)
    average = total / len(scores)
    high = max(scores)
    low = min(scores)
    score_range = high - low

    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {high}")
    print(f"Low score: {low}")
    print(f"Score range: {score_range}")

if __name__ == "__main__":
	main()