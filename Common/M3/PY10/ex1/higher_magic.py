from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    """Prende due callable e li restituisce insieme"""
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def amplified(*args, **kwargs):
        """return della v con moltiplicatore applicato"""
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def caster(*args, **kwargs):
        """returna lo spell solamente se confizione vera"""
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[Callable]) -> Callable:
    def sequence(*args, **kwargs):
        """lancia tutti gli spell e returna la lista dei risultati"""
        results = []
        for spell in spells:
            results.append(spell(*args, **kwargs))
        return results
    return sequence


if __name__ == '__main__':
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combo = spell_combiner(fireball, heal)
    res = combo("Dragon")
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("Testing power amplifier...")

    def base_damage(power: int) -> int:
        return power

    big = power_amplifier(base_damage, 3)
    print(f"Original: {base_damage(10)}, Amplified: {big(10)}")

    print("Testing conditional caster...")

    def is_powerful(power: int) -> bool:
        return power >= 50

    def blast(power: int) -> str:
        return f"Blast deals {power} damage"

    cond = conditional_caster(is_powerful, blast)
    print(cond(80))
    print(cond(20))

    print("Testing spell sequence...")

    def shield(target: str) -> str:
        return f"Shield on {target}"

    seq = spell_sequence([fireball, heal, shield])
    print(seq("Mage"))
