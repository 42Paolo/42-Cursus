from mimetypes import init


class Event:
	def __init__(self, e_name: str, give_xp: int):
		self.e_name = e_name
		self.give_xp = give_xp
	

class Level:
	def __init__(self, xp: int):
		self.xp = xp
	
	@staticmethod
	def xp_required(level: int):
		return level * 100


class Player:
	def __init__(self, u_nickname: str, level: int, xp: int):
		self.u_nickname = u_nickname
		self.level = 1
		xp = 0
	
	def 
	
	def add_xp(self, amount: int):
		self.xp += amount
		while(self.xp > Level.xp_required(self.level)):
			self.xp -= Level.xp_required(self.level)
			self.level += 1
			print(f"[{self.u_nickname}] - Leveled up to: {self.level} Level")
	


def main():
	print("=== Game Data Stream Processor ===\n")


if __name__ == "__main__":
	main()