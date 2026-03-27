from .AggressiveStrategy import AggressiveStrategy
from .FantasyCardFactory import FantasyCardFactory
from .GameEngine import GameEngine


def _format_hand(hand: list) -> str:
    parts = []
    i = 0
    while i < len(hand):
        card = hand[i]
        parts.append(f"{card.name} ({card.cost})")
        i += 1
    return ", ".join(parts)


def main() -> None:
    print("=== DataDeck Game Engine ===")
    print("Configuring Fantasy Card Game...")

    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()
    engine = GameEngine()
    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy: AggressiveStrategy")
    print("Available types:", factory.get_supported_types())
    print("Simulating aggressive turn...")
    print("Hand: [" + _format_hand(engine.hand) + "]")
    print("Turn execution:")
    turn = engine.simulate_turn()
    print("Strategy:", turn["strategy"])
    print("Actions:", turn["actions"])
    print("Game Report:")
    print(engine.get_engine_status())
    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")
    print(
        "How do Abstract Factory and Strategy patterns work together? "
        "What makes this combination powerful for game engine systems?"
    )


if __name__ == "__main__":
    main()
