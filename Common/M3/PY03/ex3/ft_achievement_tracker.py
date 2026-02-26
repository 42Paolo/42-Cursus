def main() -> None:
    print("=== Achievement Tracker System ===")
    alice = set(
        ["first_kill", "level_10", "treasure_hunter", "speed_demon"]
    )
    bob = set(["first_kill", "level_10", "boss_slayer", "collector"])
    charlie = set(
        [
            "level_10",
            "treasure_hunter",
            "boss_slayer",
            "speed_demon",
            "perfectionist",
        ]
    )
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

    rare = (
        alice.difference(bob).difference(charlie)
        .union(bob.difference(alice).difference(charlie))
        .union(charlie.difference(alice).difference(bob))
    )
    print("Rare achievements (1 player):", rare)

    alice_bob_common = alice.intersection(bob)
    alice_unique = alice.difference(bob)
    bob_unique = bob.difference(alice)
    print("Alice vs Bob common:", alice_bob_common)
    print("Alice unique:", alice_unique)
    print("Bob unique:", bob_unique)


main()
