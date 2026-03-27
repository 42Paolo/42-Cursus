from .GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        available_mana = 5
        cards_played = []
        damage_dealt = 0

        i = 0
        while i < len(hand):
            card = hand[i]
            if card.cost <= available_mana:
                cards_played.append(card.name)
                available_mana -= card.cost
                if card.name == "Goblin Warrior":
                    damage_dealt += 2
                elif card.name == "Lightning Bolt":
                    damage_dealt += 3
                battlefield.append(card)
                hand.pop(i)
                continue
            i += 1

        return {
            "cards_played": cards_played,
            "mana_used": 5 - available_mana,
            "targets_attacked": ["Enemy Player"],
            "damage_dealt": damage_dealt,
        }

    def get_strategy_name(self) -> str:
        return "AggressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        return available_targets
