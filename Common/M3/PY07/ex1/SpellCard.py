# def __init__(self, name: str, cost: int, rarity: str, effect_type: str)
# def play(self, game_state: dict) -> dict
# def resolve_effect(self, targets: list) -> dict

from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, effect_type: str):
        super().__init__(name, cost, rarity)
        if effect_type.strip() == "":
            raise ValueError("effect_type cannot be empty")
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        available_mana = game_state.get("available_mana", 0)
        if not self.is_playable(available_mana):
            return {}
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": self.resolve_effect([]).get("effect", ""),
        }

    def resolve_effect(self, targets: list) -> dict:
        if self.effect_type == "damage":
            effect = "Deal 3 damage to target"
        elif self.effect_type == "heal":
            effect = "Heal 3 health to target"
        elif self.effect_type == "buff":
            effect = "Give +1/+1 to target"
        elif self.effect_type == "debuff":
            effect = "Give -1/-1 to target"
        else:
            effect = "Unknown spell effect"
        return {"effect": effect, "targets": targets}
