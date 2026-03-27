from .CardFactory import CardFactory
from .GameStrategy import GameStrategy


class GameEngine:
    def __init__(self) -> None:
        self.factory: CardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.turns_simulated = 0
        self.total_damage = 0
        self.cards_created = 0
        self.hand = []
        self.battlefield = []

    def configure_engine(
        self, factory: CardFactory, strategy: GameStrategy
    ) -> None:
        self.factory = factory
        self.strategy = strategy
        self.hand = [
            factory.create_creature(),
            factory.create_creature(),
            factory.create_spell(),
        ]
        self.cards_created = 3

    def simulate_turn(self) -> dict:
        if self.strategy is None:
            raise ValueError("Engine not configured")
        result = self.strategy.execute_turn(self.hand, self.battlefield)
        self.turns_simulated += 1
        self.total_damage += result.get("damage_dealt", 0)
        return {
            "strategy": self.strategy.get_strategy_name(),
            "actions": result,
        }

    def get_engine_status(self) -> dict:
        if self.strategy is None:
            strategy_name = ""
        else:
            strategy_name = self.strategy.get_strategy_name()
        return {
            "turns_simulated": self.turns_simulated,
            "strategy_used": strategy_name,
            "total_damage": self.total_damage,
            "cards_created": self.cards_created,
        }
