# def add_card(self, card: Card) -> None
# def remove_card(self, card_name: str) -> bool
# def shuffle(self) -> None
# def draw_card(self) -> Card
# def get_deck_stats(self) -> dict

import random

from ex0.Card import Card
from ex0.CreatureCard import CreatureCard
from .SpellCard import SpellCard
from .ArtifactCard import ArtifactCard


class Deck:
    def __init__(self) -> None:
        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        i = 0
        while i < len(self.cards):
            if self.cards[i].name == card_name:
                self.cards.pop(i)
                return True
            i += 1
        return False

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        if len(self.cards) == 0:
            raise IndexError("Cannot draw from empty deck")
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        total_cards = len(self.cards)
        creatures = 0
        spells = 0
        artifacts = 0
        total_cost = 0

        i = 0
        while i < total_cards:
            card = self.cards[i]
            total_cost += card.cost
            if isinstance(card, CreatureCard):
                creatures += 1
            elif isinstance(card, SpellCard):
                spells += 1
            elif isinstance(card, ArtifactCard):
                artifacts += 1
            i += 1

        if total_cards == 0:
            avg_cost = 0.0
        else:
            avg_cost = total_cost / total_cards

        return {
            "total_cards": total_cards,
            "creatures": creatures,
            "spells": spells,
            "artifacts": artifacts,
            "avg_cost": avg_cost,
        }
