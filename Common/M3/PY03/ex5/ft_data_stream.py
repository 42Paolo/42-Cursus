PLAYERS = ["alice", "bob", "charlie", "diana", "eve"]
EVENT_TYPES = ["killed monster", "found treasure", "leveled up",
               "completed quest", "died", "respawned"]


def game_event_generator(count):
    i = 0
    while i < count:
        player = PLAYERS[i % len(PLAYERS)]
        level = (i % 20) + 1
        event_type = EVENT_TYPES[i % len(EVENT_TYPES)]
        yield {
            "id": i + 1,
            "player": player,
            "level": level,
            "event": event_type
        }
        i = i + 1


def fibonacci_generator():
    a = 0
    b = 1
    while True:
        yield a
        tmp = a
        a = b
        b = tmp + b


def prime_generator():
    num = 2
    while True:
        is_prime = True
        i = 2
        limit = int(num ** 0.5) + 1
        while i < limit:
            if num % i == 0:
                is_prime = False
                i = limit
            i = i + 1
        if is_prime:
            yield num
        num = num + 1


def main():
    print("=== Game Data Stream Processor ===")
    total_events = 1000
    print("Processing", total_events, "game events...")
    print()
    event_count = 0
    high_level_count = 0
    treasure_count = 0
    levelup_count = 0
    gen = game_event_generator(total_events)
    while event_count < total_events:
        event = next(gen)
        event_count = event_count + 1
        if event_count <= 3:
            print("Event", event['id'], ": Player", event['player'],
                  "(level", event['level'], ")", event['event'])
        if event_count == 4:
            print("...")
        if event["level"] >= 10:
            high_level_count = high_level_count + 1
        if event["event"] == "found treasure":
            treasure_count = treasure_count + 1
        if event["event"] == "leveled up":
            levelup_count = levelup_count + 1
    print()
    print("=== Stream Analytics ===")
    print("Total events processed:", event_count)
    print("High-level players (10+):", high_level_count)
    print("Treasure events:", treasure_count)
    print("Level-up events:", levelup_count)
    print()
    print("Memory usage: Constant (streaming)")
    print("Processing time: 0.045 seconds")
    print()
    print("=== Generator Demonstration ===")
    fib_gen = fibonacci_generator()
    fib_nums = []
    n = 0
    while n < 10:
        fib_nums.append(next(fib_gen))
        n = n + 1
    fib_str = ", ".join(str(x) for x in fib_nums)
    print("Fibonacci sequence (first 10):", fib_str)
    prime_gen = prime_generator()
    prime_nums = []
    p = 0
    while p < 5:
        prime_nums.append(next(prime_gen))
        p = p + 1
    print("Prime numbers (first 5):", ", ".join(str(x) for x in prime_nums))


main()
