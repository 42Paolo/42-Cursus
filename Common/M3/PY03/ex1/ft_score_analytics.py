import sys


def ft_len(obj):
    count = 0
    for _ in obj:
        count += 1
    return count


def main():
    print("=== Player Score Analytics ===")

    argc = ft_len(sys.argv)

    if argc == 1:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return

    tot = 0
    scores = sys.argv[1:]
    count_scores = ft_len(scores)

    try:
        first = int(scores[0])
    except ValueError:
        print("Error: all scores must be integers")
        return

    max_score = first
    min_score = first

    print("Scores processed: [", end="")

    for arg in scores:
        try:
            value = int(arg)
        except ValueError:
            print("\nError: all scores must be integers")
            return

        print(f"{value} ", end="")

        tot += value

        if value > max_score:
            max_score = value
        if value < min_score:
            min_score = value

    print("]")

    average = tot / count_scores
    score_range = max_score - min_score

    print(f"Total players: {count_scores}")
    print(f"Total score: {tot}")
    print(f"Average score: {average}")
    print(f"High score: {max_score}")
    print(f"Low score: {min_score}")
    print(f"Score range: {score_range}")


if __name__ == "__main__":
    main()
