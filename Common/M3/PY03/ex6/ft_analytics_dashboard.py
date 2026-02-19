def main():
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
    high_scorers = []
    i = 0
    while i < len(players_data):
        if players_data[i]["score"] > 2000:
            high_scorers.append(players_data[i]["name"])
        i = i + 1
    print("High scorers (>2000):", high_scorers)
    scores_doubled = []
    j = 0
    while j < len(players_data):
        if players_data[j]["active"]:
            scores_doubled.append(players_data[j]["score"] * 2)
        j = j + 1
    print("Scores doubled:", scores_doubled)
    active_players = []
    k = 0
    while k < len(players_data):
        if players_data[k]["active"]:
            active_players.append(players_data[k]["name"])
        k = k + 1
    print("Active players:", active_players)
    print()
    print("=== Dict Comprehension Examples ===")
    player_scores = {}
    idx = 0
    while idx < 3 and idx < len(players_data):
        p = players_data[idx]
        player_scores[p["name"]] = p["score"]
        idx = idx + 1
    print("Player scores:", player_scores)

    def get_category(score):
        if score > 2000:
            return "high"
        elif score > 1500:
            return "medium"
        return "low"

    categories = ["high", "medium", "low"]
    score_categories = {}
    c = 0
    while c < len(categories):
        cat = categories[c]
        cnt = 0
        d = 0
        while d < len(players_data):
            if get_category(players_data[d]["score"]) == cat:
                cnt = cnt + 1
            d = d + 1
        if cnt > 0:
            score_categories[cat] = cnt
        c = c + 1
    print("Score categories:", score_categories)
    achievement_counts = {}
    a = 0
    while a < 3 and a < len(players_data):
        p = players_data[a]
        achievement_counts[p["name"]] = len(p["achievements"])
        a = a + 1
    print("Achievement counts:", achievement_counts)
    print()
    print("=== Set Comprehension Examples ===")
    unique_players = set()
    u = 0
    while u < len(players_data):
        unique_players.add(players_data[u]["name"])
        u = u + 1
    print("Unique players:", unique_players)
    unique_achievements = set()
    ua = 0
    while ua < len(players_data):
        ach_list = players_data[ua]["achievements"]
        ab = 0
        while ab < len(ach_list):
            if ach_list[ab] in ["first_kill", "level_10", "boss_slayer"]:
                unique_achievements.add(ach_list[ab])
            ab = ab + 1
        ua = ua + 1
    print("Unique achievements:", unique_achievements)
    active_regions = set()
    ar = 0
    while ar < len(players_data):
        if players_data[ar]["active"]:
            active_regions.add(players_data[ar]["region"])
        ar = ar + 1
    print("Active regions:", active_regions)
    print()
    print("=== Combined Analysis ===")
    total_players = len(unique_players)
    all_achievements = set()
    aa = 0
    while aa < len(players_data):
        ach_list = players_data[aa]["achievements"]
        ab = 0
        while ab < len(ach_list):
            all_achievements.add(ach_list[ab])
            ab = ab + 1
        aa = aa + 1
    total_unique = len(all_achievements)
    all_scores = []
    s = 0
    while s < len(players_data):
        all_scores.append(players_data[s]["score"])
        s = s + 1
    avg_score = sum(all_scores) / len(all_scores)
    top = players_data[0]
    t = 1
    while t < len(players_data):
        if players_data[t]["score"] > top["score"]:
            top = players_data[t]
        t = t + 1
    top_ach = len(top["achievements"])
    print("Total players:", total_players)
    print("Total unique achievements:", total_unique)
    print("Average score:", avg_score)
    print("Top performer:", top['name'], "(", top['score'], "points,",
          top_ach, "achievements)")


main()
