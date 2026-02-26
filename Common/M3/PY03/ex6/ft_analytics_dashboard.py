import random
from typing import Generator


class Game():
    NAMES = ["CSGO", "Zelda", "DrugDeal", "SuperSmashBros", "LOL"]
    CATEGORIES = ["Action", "Indie", "Horror", "Logic"]

    def __init__(self, name: str, category: str):
        self.name = name
        self.category = category


class User():
    NAMES = ["alice", "bob", "charlie", "diana", "ethan", "luna", "marco", "sofia", "leo", "nina"]
    REGIONS = ["north", "east", "central", "south", "west"]
    ACHIEVEMENTS = ["first_kill", "level_10", "boss_slayer", "speedrun", "no_damage", "collector"]

    def __init__(self, name: str, region: str, days_not_log: int):
        self.name = name
        self.region = region
        self.days_not_log = days_not_log
        self.score = 0
        self.achievements = set()

    def add_achievement(self, achievement: str):
        self.achievements.add(achievement)


def game_generator(n: int) -> Generator[Game, None, None]:
    for _ in range(n):
        yield Game(random.choice(Game.NAMES), random.choice(Game.CATEGORIES))


def user_generator(n: int) -> Generator[User, None, None]:
    names = random.sample(User.NAMES, min(n, len(User.NAMES)))
    for i in range(n):
        u = User(
            name=names[i],
            region=random.choice(User.REGIONS),
            days_not_log=random.randint(0, 15)
        )
        u.score = random.randint(500, 3000)
        for ach in random.sample(User.ACHIEVEMENTS, random.randint(1, len(User.ACHIEVEMENTS))):
            u.add_achievement(ach)
        yield u


def main():
    print("=== Game Analytics Dashboard ===")

    users = list(user_generator(6))

    print("=== List Comprehension Examples ===")

    high_scorers = [u.name for u in users if u.score > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [u.score * 2 for u in users if u.score > 2000]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [u.name for u in users if u.days_not_log <= 5]
    print(f"Active players: {active_players}")

    print("=== Dict Comprehension Examples ===")

    player_scores = {u.name: u.score for u in users if u.score > 1500}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high":   len([u for u in users if u.score > 2000]),
        "medium": len([u for u in users if 1500 <= u.score <= 2000]),
        "low":    len([u for u in users if u.score < 1500]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {u.name: len(u.achievements) for u in users if u.score > 1500}
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")

    unique_players = {u.name for u in users}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for u in users for a in u.achievements}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {u.region for u in users if u.days_not_log <= 5}
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")
a
    total_players = len(users)
    total_unique_achievements = len({a for u in users for a in u.achievements})
    avg_score = sum(u.score for u in users) / total_players
    top = max(users, key=lambda u: u.score)

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top.name} ({top.score} points, {len(top.achievements)} achievements)")


if __name__ == "__main__":
    main()