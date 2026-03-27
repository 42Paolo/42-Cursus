# def __init__(
#     self, name: str, cost: int, rarity: str, durability: int, effect: str
# )
# def play(self, game_state: dict) -> dict
# def activate_ability(self) -> dict

from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(
        self, name: str, cost: int, rarity: str, durability: int, effect: str
    ):
        super().__init__(name, cost, rarity)
        if durability <= 0:
            raise ValueError("durability must be positive")
        if effect.strip() == "":
            raise ValueError("effect cannot be empty")
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.activate_ability().get("effect", ""),
        }

    def activate_ability(self) -> dict:
        return {
            "effect": f"Permanent: {self.effect}",
            "durability": self.durability,
        }
