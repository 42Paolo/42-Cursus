class Game():
	def __init__(self, name: str, score: int, achivments: int):
		self.name = name
		self.score = score	
		self.achivments = achivments
		
class User():
	def __init__(self, name: str, region: str, days_not_log: int):
		self.name = name
		self.region = region
		self.days_not_log = days_not_log
		self.scores = {}

	def set_score(self, game: Game, score: int):
		self.scores[game.name	] = score
	
	def get_score(self, game: Game):
		return self.scores.get(game.name, 0)

def main():
	print("=== Game Analytics Dashboard ===\n")
	print("=== List Comprehension Examples ===")

if __name__ == "__main__":
	main()