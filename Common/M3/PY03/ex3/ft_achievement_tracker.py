def main() -> None:
    print("=== Achievement Tracker System ===")

    alice: set[str] = {
        'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'
    }
    bob: set[str] = {
        'first_kill', 'level_10', 'boss_slayer', 'collector'
    }
    charlie: set[str] = {
        'level_10', 'treasure_hunter', 'boss_slayer',
        'speed_demon', 'perfectionist'
    }

    print(f"Player alice achievements: {alice}")
    print(f"Player bob achievements: {bob}")
    print(f"Player charlie achievements: {charlie}")

    print()
    print("=== Achievement Analytics ===")

    all_achievements: set[str] = alice.union(bob).union(charlie)
    print(f"All unique achievements: {all_achievements}")
    print(f"Total unique achievements: {len(all_achievements)}")

    common_all: set[str] = alice.intersection(bob).intersection(charlie)
    print(f"Common to all players: {common_all}")

    players = [alice, bob, charlie]
    rare: set[str] = set()
    for achievement in all_achievements:
        count = 0
        for p in players:
            if achievement in p:
                count += 1
        if count == 1:
            rare.add(achievement)
    print(f"Rare achievements (1 player): {rare}")

    alice_bob_common: set[str] = alice.intersection(bob)
    alice_unique: set[str] = alice.difference(bob)
    bob_unique: set[str] = bob.difference(alice)

    print(f"Alice vs Bob common: {alice_bob_common}")
    print(f"Alice unique: {alice_unique}")
    print(f"Bob unique: {bob_unique}")


main()
