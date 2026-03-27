from ex0.CreatureCard import CreatureCard

from .ArtifactCard import ArtifactCard
from .Deck import Deck
from .SpellCard import SpellCard


def main() -> None:
    print("=== DataDeck Deck Builder ===")
    print("Building deck with different card types...")

    deck = Deck()
    deck.add_card(CreatureCard("Fire Dragon", 5, "Legendary", 7, 5))
    deck.add_card(SpellCard("Lightning Bolt", 3, "Common", "damage"))
    deck.add_card(
        ArtifactCard("Mana Crystal", 2, "Rare", 3, "+1 mana per turn")
    )

    print("Deck stats:", deck.get_deck_stats())
    deck.shuffle()

    print("Drawing and playing cards:")
    available_mana = 10
    i = 0
    while i < 3:
        card = deck.draw_card()
        card_type = card.__class__.__name__.replace("Card", "")
        print(f"Drew: {card.name} ({card_type})")
        print("Play result:", card.play({"available_mana": available_mana}))
        i += 1

    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
