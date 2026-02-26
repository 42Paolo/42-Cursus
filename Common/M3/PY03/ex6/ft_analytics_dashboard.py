class User:
    NAMES = [
        "alice",
        "bob",
        "charlie",
        "diana",
        "ethan",
        "luna",
        "marco",
        "sofia",
        "leo",
        "nina",
    ]
    REGIONS = ["north", "east", "central", "south", "west"]
    ACHIEVEMENTS = [
        "first_kill",
        "level_10",
        "boss_slayer",
        "speedrun",
        "no_damage",
        "collector",
    ]

    def __init__(
        self, name: str, region: str, days_not_log: int, score: int
    ):
        self.name = name
        self.region = region
        self.days_not_log = days_not_log
        self.score = score
        self.achievements = []


def build_users() -> list:
    users = [
        User("alice", "north", 2, 2300),
        User("bob", "east", 5, 1800),
        User("charlie", "central", 3, 2150),
        User("diana", "north", 8, 2050),
        User("ethan", "west", 12, 900),
        User("luna", "central", 1, 1050),
    ]
    users[0].achievements = [
        "first_kill",
        "level_10",
        "boss_slayer",
        "speedrun",
        "collector",
    ]
    users[1].achievements = [
        "first_kill",
        "level_10",
        "no_damage",
    ]
    users[2].achievements = [
        "first_kill",
        "level_10",
        "boss_slayer",
        "speedrun",
        "no_damage",
        "collector",
        "extra",
    ]
    users[3].achievements = ["first_kill", "boss_slayer"]
    users[4].achievements = ["first_kill"]
    users[5].achievements = ["level_10"]
    return users


def main() -> None:
    users = build_users()

    print("=== Game Analytics Dashboard ===")

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
        "high": len([u for u in users if u.score > 2000]),
        "medium": len([u for u in users if 1500 <= u.score <= 2000]),
        "low": len([u for u in users if u.score < 1500]),
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        u.name: len(u.achievements) for u in users if u.score > 1500
    }
    print(f"Achievement counts: {achievement_counts}")

    print("=== Set Comprehension Examples ===")

    unique_players = {u.name for u in users}
    print(f"Unique players: {unique_players}")

    unique_achievements = {a for u in users for a in u.achievements}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {u.region for u in users if u.days_not_log <= 5}
    print(f"Active regions: {active_regions}")

    print("=== Combined Analysis ===")

    total_players = len(users)
    total_unique_achievements = len(
        {a for u in users for a in u.achievements}
    )
    avg_score = sum(u.score for u in users) / total_players

    top = users[0]
    for u in users:
        if u.score > top.score:
            top = u

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique_achievements}")
    print(f"Average score: {avg_score}")
    print(
        f"Top performer: {top.name} "
        f"({top.score} points, {len(top.achievements)} achievements)"
    )


if __name__ == "__main__":
    main()
