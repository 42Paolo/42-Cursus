from ex0.Card import Card

from .Combatable import Combatable
from .Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def __init__(
        self, name: str, cost: int, rarity: str, attack: int, health: int
    ):
        super().__init__(name, cost, rarity)
        self.attack_power = attack
        self.health = health
        self.total_mana = 0

    def play(self, game_state: dict) -> dict:
        return {
            "card_played": self.name,
            "mana_used": self.cost,
            "effect": (
                "Elite card enters battle with combat and magic abilities"
            ),
        }

    def attack(self, target) -> dict:
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.attack_power,
            "combat_type": "melee",
        }

    def defend(self, incoming_damage: int) -> dict:
        blocked = 0
        if incoming_damage > 0:
            blocked = 3
        taken = incoming_damage - blocked
        if taken < 0:
            taken = 0
        self.health -= taken
        return {
            "defender": self.name,
            "damage_taken": taken,
            "damage_blocked": blocked,
            "still_alive": self.health > 0,
        }

    def get_combat_stats(self) -> dict:
        return {"attack": self.attack_power, "health": self.health}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": 4,
        }

    def channel_mana(self, amount: int) -> dict:
        self.total_mana += amount
        return {"channeled": amount, "total_mana": self.total_mana}

    def get_magic_stats(self) -> dict:
        return {"total_mana": self.total_mana}
