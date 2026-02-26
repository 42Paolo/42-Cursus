import random
from typing import Generator


class Game():
	def __init__(self, name: str, score: int, achivments: int, category: str):
		self.name = name
		self.score = score	
		self.achivments = achivments
		self.category = category
	
	NAME_GAMES = ["CSGO", "Zelda", "DrugDeal", "SuperSmashBros", "LOL"]
	CATEGORIES = ["Action", "Indie", "Horror", "Logic"]


def game_generator(n: int) -> Generator[Game, None, None]:
	for _ in range(n):
		name = random.choice(Game.NAME_GAMES)
		score = random.randint(0, 5000)
		achivments = random.randint(0,50)
		category = random.choice(Game.CATEGORIES)

		yield Game(name, score, achivments, category)


class User():
	def __init__(self, name: str, region: str, days_not_log: int):
		self.name = name
		self.region = region
		self.days_not_log = days_not_log
		self.scores = {}

	NAME = ["Alice","Bob","Charlie","Diana","Ethan","Luna","Marco","Sofia","Leo","Nina"]

	REGION = ["EU-West","EU-East","NA-East","NA-West","Asia","South-America","Oceania","Middle-East"]


	def set_score(self, game: Game, score: int):
		self.scores[game.name] = score
	
	def get_score(self, game: Game):
		return self.scores.get(game.name, 0)


def u_gen(n: int) -> Generator[User, None, None]:
	for _ in range(n):
		name = random.choice(User.NAME)
		region = random.choice(User.REGION)
		days_not_log = random.randint(0, 50)

		yield User(name, region, days_not_log)


def main():
	print("=== Game Analytics Dashboard ===\n")

	users = list(u_gen(30))
	games = list(game_generator(80))

	for user in users:
		num_games = random.randint(5, 15)
		chosen_games = random.sample(games, num_games)

		for game in chosen_games:
			score = random.randint(0, 1000)
			user.set_score(game, score)

	for user in users[:5]:
		print(user.name, "-", user.region)
		for game_name, score in user.scores.items():
			print("  ", game_name, ":", score)
		print()


if __name__ == "__main__":
	main()