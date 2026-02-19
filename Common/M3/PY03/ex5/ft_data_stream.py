import sys
from typing import Generator

PLAYERS = ["alice", "bob", "charlie", "diana", "eve"]
EVENTS = [
    "killed monster", "found treasure", "leveled up", "completed quest"
]


def game_events(count: int) -> Generator[dict, None, None]:
    for i in range(count):
        yield {
            "id": i + 1,
            "player": PLAYERS[i % len(PLAYERS)],
            "level": (i % 20) + 1,
            "event": EVENTS[i % len(EVENTS)],
        }


def fibonacci() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def primes() -> Generator[int, None, None]:
    n = 2
    while True:
        is_prime = True
        for d in range(2, int(n ** 0.5) + 1):
            if n % d == 0:
                is_prime = False
                break
        if is_prime:
            yield n
        n += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")
    print()

    count = 1000
    if len(sys.argv) > 1:
        try:
            count = int(sys.argv[1])
        except ValueError:
            pass

    print(f"Processing {count} game events...")
    print()

    total = 0
    high_level = 0
    treasure = 0
    levelups = 0

    for event in game_events(count):
        total += 1
        if total <= 3:
            print(
                f"Event {event['id']}: Player {event['player']}"
                f" (level {event['level']}) {event['event']}"
            )
        elif total == 4:
            print("...")
        if event["level"] >= 10:
            high_level += 1
        if event["event"] == "found treasure":
            treasure += 1
        if event["event"] == "leveled up":
            levelups += 1

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {total}")
    print(f"High-level players (10+): {high_level}")
    print(f"Treasure events: {treasure}")
    print(f"Level-up events: {levelups}")
    print("Memory usage: Constant (streaming)")

    print()
    print("=== Generator Demonstration ===")
    fib = fibonacci()
    fib_list = []
    for _ in range(10):
        fib_list.append(next(fib))
    fib_str = ', '.join(str(x) for x in fib_list)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_gen = primes()
    prime_list = []
    for _ in range(5):
        prime_list.append(next(prime_gen))
    print(f"Prime numbers (first 5): {', '.join(str(x) for x in prime_list)}")


main()
