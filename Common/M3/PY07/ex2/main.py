from .EliteCard import EliteCard


def main() -> None:
    print("=== DataDeck Ability System ===")
    print("EliteCard capabilities:")
    print("- Card: ['play', 'get_card_info', 'is_playable']")
    print("- Combatable: ['attack', 'defend', 'get_combat_stats']")
    print("- Magical: ['cast_spell', 'channel_mana', 'get_magic_stats']")

    card = EliteCard("Arcane Warrior", 4, "Epic", 5, 10)
    print("Playing Arcane Warrior (Elite Card):")
    print("Combat phase:")
    print("Attack result:", card.attack("Enemy"))
    print("Defense result:", card.defend(5))
    print("Magic phase:")
    print("Spell cast:", card.cast_spell("Fireball", ["Enemy1", "Enemy2"]))
    print("Mana channel:", card.channel_mana(3))
    print("Multiple interface implementation successful!")
    print(
        "How do multiple interfaces enable flexible card design? "
        "What are the advantages of separating combat and magic concerns?"
    )


if __name__ == "__main__":
    main()
