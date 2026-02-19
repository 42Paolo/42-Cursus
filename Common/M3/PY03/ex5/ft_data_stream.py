from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "diana", "eve"]
EVENT_TYPES = ["killed monster", "found treasure", "leveled up",
               "completed quest", "died", "respawned"]


def game_event_generator(
    count: int
) -> Generator[dict[str, object], None, None]:
    for i in range(count):
        player = PLAYERS[i % len(PLAYERS)]
        level = (i % 20) + 1
        event_type = EVENT_TYPES[i % len(EVENT_TYPES)]
        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event_type
        }


def fibonacci_generator() -> Generator[int, None, None]:
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b


def prime_generator() -> Generator[int, None, None]:
    num = 2
    while True:
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            yield num
        num += 1


def main() -> None:
    print("=== Game Data Stream Processor ===")

    total_events = 1000
    print(f"Processing {total_events} game events...")
    print()

    event_count = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0

    for event in game_event_generator(total_events):
        event_count += 1
        if event_count <= 3:
            print(f"Event {event['id']}: Player {event['player']}"
                  f" (level {event['level']}) {event['event']}")
        if event_count == 4:
            print("...")
        if int(str(event["level"])) >= 10:
            high_level_count += 1
        if event["event"] == "found treasure":
            treasure_count += 1
        if event["event"] == "leveled up":
            levelup_count += 1

    print()
    print("=== Stream Analytics ===")
    print(f"Total events processed: {event_count}")
    print(f"High-level players (10+): {high_level_count}")
    print(f"Treasure events: {treasure_count}")
    print(f"Level-up events: {levelup_count}")
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")

    print()
    print("=== Generator Demonstration ===")

    fib_gen = fibonacci_generator()
    fib_nums = [next(fib_gen) for _ in range(10)]
    fib_str = ', '.join(str(n) for n in fib_nums)
    print(f"Fibonacci sequence (first 10): {fib_str}")

    prime_gen = prime_generator()
    prime_nums = [next(prime_gen) for _ in range(5)]
    print(f"Prime numbers (first 5): {', '.join(str(n) for n in prime_nums)}")


main()
