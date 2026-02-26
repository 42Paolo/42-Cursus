from typing import Generator


PLAYERS = ["alice", "bob", "charlie", "diana", "eve"]
CATEGORIES = ["kill", "treasure", "quest"]
XP_PER_CATEGORY = {
	"kill": 10,
	"treasure": 100,
	"quest": 150
}
EVENT_DESCRIPTIONS = {
	"kill": "killed monster",
	"treasure": "found treasure",
	"quest": "leveled up"
}


class PseudoRandom:
	def __init__(self, seed: int = 42):
		self._seed = seed

	def next(self) -> int:
		self._seed = (self._seed * 1103515245 + 12345) & 0x7FFFFFFF
		return self._seed

	def pick_from(self, lst: list) -> str:
		return lst[self.next() % len(lst)]

	def pick_int(self, low: int, high: int) -> int:
		return low + self.next() % (high - low + 1)


class Level:
	@staticmethod
	def xp_required(level: int) -> int:
		return level * 100


class Event:
	ALLOWED_CATEGORY = CATEGORIES

	def __init__(self, e_category: str):
		if e_category not in Event.ALLOWED_CATEGORY:
			raise ValueError(f"Invalid category: {e_category!r}")
		self.e_category = e_category
		self.xp = XP_PER_CATEGORY[e_category]
		self.description = EVENT_DESCRIPTIONS[e_category]


class Player:
	def __init__(self, u_nickname: str):
		self.u_nickname = u_nickname
		self.xp = 0
		self.level = 1
		self.e_done = 0

	def add_xp(self, amount: int) -> None:
		self.xp += amount
		while self.xp >= Level.xp_required(self.level):
			self.xp -= Level.xp_required(self.level)
			self.level += 1


def _is_prime(n: int) -> bool:
	if n < 2:
		return False
	i = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += 1
	return True


def game_event_stream(n_events: int) -> Generator[dict, None, None]:
	players = {}
	for name in PLAYERS:
		players[name] = Player(name)
	rng = PseudoRandom(seed=42)

	for i in range(n_events):
		player = players[rng.pick_from(PLAYERS)]
		event = Event(rng.pick_from(CATEGORIES))
		level_boost = rng.pick_int(1, 20)
		player.add_xp(event.xp + level_boost)
		player.e_done += 1
		yield {
			"index": i + 1,
			"player": player.u_nickname,
			"level": player.level,
			"category": event.e_category,
			"description": event.description,
			"xp": event.xp
		}


def high_level_filter(stream: Generator, min_level: int = 10) -> Generator[dict, None, None]:
	for event in stream:
		if event["level"] >= min_level:
			yield event


def fibonacci() -> Generator[int, None, None]:
	a, b = 0, 1
	while True:
		yield a
		a, b = b, a + b


def prime_numbers() -> Generator[int, None, None]:
	n = 2
	while True:
		if _is_prime(n):
			yield n
		n += 1


def sum_e_level(*players: Player) -> Generator[int, None, None]:
	for p in players:
		yield p.level


def _format_event(event: dict) -> str:
	return (f"Event {event['index']}: Player {event['player']} "
	        f"(level {event['level']}) {event['description']}")


def main() -> None:
	print("=== Game Data Stream Processor ===\n")
	N_EVENTS = 1000
	PREVIEW_COUNT = 3
	print(f"Processing {N_EVENTS} game events...\n")

	total = 0
	high_level_count = 0
	treasure_count = 0
	levelup_count = 0

	stream = game_event_stream(N_EVENTS)
	for event in stream:
		total += 1
		if total <= PREVIEW_COUNT:
			print(_format_event(event))
		elif total == PREVIEW_COUNT + 1:
			print("...\n")
		if event["level"] >= 10:
			high_level_count += 1
		if event["category"] == "treasure":
			treasure_count += 1
		if event["category"] == "quest":
			levelup_count += 1

	print("=== Stream Analytics ===")
	print(f"Total events processed: {total}")
	print(f"High-level players (10+): {high_level_count}")
	print(f"Treasure events: {treasure_count}")
	print(f"Level-up events: {levelup_count}")
	print(f"Memory usage: Constant (streaming)\n")

	print("=== Generator Demonstration ===")
	fib_gen = fibonacci()
	fib_str = ""
	for _ in range(10):
		val = next(fib_gen)
		if fib_str != "":
			fib_str += ", "
		fib_str += f"{val}"
	print(f"Fibonacci sequence (first 10): {fib_str}")

	prime_gen = prime_numbers()
	prime_str = ""
	for _ in range(5):
		val = next(prime_gen)
		if prime_str != "":
			prime_str += ", "
		prime_str += f"{val}"
	print(f"Prime numbers (first 5): {prime_str}")


if __name__ == "__main__":
	main()
