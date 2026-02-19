def main():
    print("=== Achievement Tracker System ===")
    alice = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
    bob = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
    charlie = {'level_10', 'treasure_hunter', 'boss_slayer',
               'speed_demon', 'perfectionist'}
    print("Player alice achievements:", alice)
    print("Player bob achievements:", bob)
    print("Player charlie achievements:", charlie)
    print()
    print("=== Achievement Analytics ===")
    all_achievements = alice.union(bob).union(charlie)
    print("All unique achievements:", all_achievements)
    print("Total unique achievements:", len(all_achievements))
    common_all = alice.intersection(bob).intersection(charlie)
    print("Common to all players:", common_all)
    players = [alice, bob, charlie]
    rare = set()
    ach_list = list(all_achievements)
    i = 0
    while i < len(ach_list):
        achievement = ach_list[i]
        count = 0
        j = 0
        while j < len(players):
            if achievement in players[j]:
                count = count + 1
            j = j + 1
        if count == 1:
            rare.add(achievement)
        i = i + 1
    print("Rare achievements (1 player):", rare)
    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print("Alice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


main()
