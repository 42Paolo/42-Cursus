from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")
    print()
    print("Testing Abstract Base Class Design:")
    print()

    print("CreatureCard Info:")
    fire_dragon = CreatureCard(
        name="Fire Dragon",
        cost=5,
        rarity="Legendary",
        attack=7,
        health=5,
    )
    print(fire_dragon.get_card_info())

    print()
    print("Playing Fire Dragon with 6 mana available:")
    available_mana = 6
    playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {playable}")
    if playable:
        game_state = {"available_mana": available_mana}
        print("Play result:", fire_dragon.play(game_state))
        print()
        print("Fire Dragon attacks Goblin Warrior:")
        print("Attack result:", fire_dragon.attack_target("Goblin Warrior"))

    print()
    print("Testing insufficient mana (3 available):")
    available_mana = 3
    playable = fire_dragon.is_playable(available_mana)
    print(f"Playable: {playable}")

    print("Abstract pattern successfully demonstrated!")
    print(
        "How do abstract base classes ensure consistency across different card types? "
        "What happens if you try to create a Card directly without implementing required methods?"
    )


if __name__ == "__main__":
    main()