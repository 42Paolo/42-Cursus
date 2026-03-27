from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard

from .CardFactory import CardFactory


class FantasyCardFactory(CardFactory):
    def __init__(self) -> None:
        self.created_count = 0

    def create_creature(self, name_or_power=None):
        self.created_count += 1
        return CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    def create_spell(self, name_or_power=None):
        self.created_count += 1
        return SpellCard("Lightning Bolt", 3, "Common", "damage")

    def create_artifact(self, name_or_power=None):
        self.created_count += 1
        return ArtifactCard("Mana Ring", 2, "Rare", 3, "+1 mana per turn")

    def create_themed_deck(self, size: int) -> dict:
        hand = []
        i = 0
        while i < size:
            if i % 3 == 0:
                hand.append(self.create_creature())
            elif i % 3 == 1:
                hand.append(self.create_spell())
            else:
                hand.append(self.create_artifact())
            i += 1
        return {"hand": hand}

    def get_supported_types(self) -> dict:
        return {
            "creatures": ["dragon", "goblin"],
            "spells": ["fireball"],
            "artifacts": ["mana_ring"],
        }
