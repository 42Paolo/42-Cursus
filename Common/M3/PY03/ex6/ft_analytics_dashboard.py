def main() -> None:
    # sample data to work with
    players_data = [
        {"name": "alice", "score": 2300, "active": True,
         "achievements": ["first_kill", "level_10", "speed_demon",
                          "boss_slayer", "perfectionist"],
         "region": "north"},
        {"name": "bob", "score": 1800, "active": True,
         "achievements": ["first_kill", "level_10", "collector"],
         "region": "east"},
        {"name": "charlie", "score": 2150, "active": True,
         "achievements": ["level_10", "treasure_hunter", "boss_slayer",
                          "speed_demon", "collector", "first_kill",
                          "perfectionist"],
         "region": "central"},
        {"name": "diana", "score": 2050, "active": False,
         "achievements": ["first_kill", "level_10"],
         "region": "north"},
    ]

    print("=== Game Analytics Dashboard ===")

    print()
    print("=== List Comprehension Examples ===")

    high_scorers = [p["name"] for p in players_data if p["score"] > 2000]
    print(f"High scorers (>2000): {high_scorers}")

    scores_doubled = [p["score"] * 2 for p in players_data if p["active"]]
    print(f"Scores doubled: {scores_doubled}")

    active_players = [p["name"] for p in players_data if p["active"]]
    print(f"Active players: {active_players}")

    # Dict comprehension examples
    print()
    print("=== Dict Comprehension Examples ===")

    player_scores = {p["name"]: p["score"] for p in players_data[:3]}
    print(f"Player scores: {player_scores}")

    def get_category(score: int) -> str:
        if score > 2000:
            return "high"
        elif score > 1500:
            return "medium"
        return "low"

    categories = ["high", "medium", "low"]
    score_categories = {
        cat: len([p for p in players_data if get_category(p["score"]) == cat])
        for cat in categories
        if any(get_category(p["score"]) == cat for p in players_data)
    }
    print(f"Score categories: {score_categories}")

    achievement_counts = {
        p["name"]: len(p["achievements"]) for p in players_data[:3]
    }
    print(f"Achievement counts: {achievement_counts}")

    print()
    print("=== Set Comprehension Examples ===")

    unique_players = {p["name"] for p in players_data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {
        ach for p in players_data
        for ach in p["achievements"]
        if ach in ["first_kill", "level_10", "boss_slayer"]
    }
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {p["region"] for p in players_data if p["active"]}
    print(f"Active regions: {active_regions}")

    print()
    print("=== Combined Analysis ===")

    total_players = len(unique_players)
    all_achievements = {
        ach for p in players_data for ach in p["achievements"]
    }
    total_unique = len(all_achievements)
    all_scores = [p["score"] for p in players_data]
    avg_score = sum(all_scores) / len(all_scores)

    top = max(players_data, key=lambda p: p["score"])
    top_ach = len(top["achievements"])

    print(f"Total players: {total_players}")
    print(f"Total unique achievements: {total_unique}")
    print(f"Average score: {avg_score}")
    print(f"Top performer: {top['name']} ({top['score']} points,"
          f" {top_ach} achievements)")


main()
