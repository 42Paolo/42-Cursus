players = [
    {
        "name": "alice", "score": 2300, "active": True, "region": "north",
        "achievements": [
            "first_kill", "level_10", "boss_slayer", "speed_demon", "collector"
        ],
    },
    {
        "name": "bob", "score": 1800, "active": True, "region": "east",
        "achievements": ["first_kill", "level_10", "treasure_hunter"],
    },
    {
        "name": "charlie", "score": 2150, "active": True, "region": "central",
        "achievements": [
            "level_10", "boss_slayer", "speed_demon", "perfectionist",
            "collector", "treasure_hunter", "guardian"
        ],
    },
    {
        "name": "diana", "score": 2050, "active": False, "region": "north",
        "achievements": ["first_kill", "level_10", "speed_demon"],
    },
]


def main() -> None:
    print("=== Game Analytics Dashboard ===")

    print()
    print("=== List Comprehension Examples ===")
    high_scorers = [p["name"] for p in players if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in players if p["score"] > 2000]
    print(f"Scores doubled: {scores_doubled}")

    active = [p["name"] for p in players if p["active"]]
    print(f"Active players: {active}")

    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {p["name"]: p["score"] for p in players if p["active"]}
    print(f"Player scores: {player_scores}")

    score_categories = {
        "high": len([p for p in players if p["score"] >= 2100]),
        "medium": len([p for p in players if 1800 <= p["score"] < 2100]),
        "low": len([p for p in players if p["score"] < 1800]),
    }
    print(f"Score categories: {score_categories}")

    ach_counts = {p["name"]: len(p["achievements"]) for p in players}
    print(f"Achievement counts: {ach_counts}")

    print()
    print("=== Set Comprehension Examples ===")
    unique_players = {p["name"] for p in players}
    print(f"Unique players: {unique_players}")

    unique_ach = {a for p in players for a in p["achievements"]}
    print(f"Unique achievements: {unique_ach}")

    active_regions = {p["region"] for p in players if p["active"]}
    print(f"Active regions: {active_regions}")

    print()
    print("=== Combined Analysis ===")
    print(f"Total players: {len(players)}")
    print(f"Total unique achievements: {len(unique_ach)}")
    scores = [p["score"] for p in players]
    print(f"Average score: {sum(scores) / len(scores)}")
    top = max(players, key=lambda p: len(p["achievements"]))
    print(
        f"Top performer: {top['name']} "
        f"({top['score']} points, {len(top['achievements'])} achievements)"
    )


main()
