def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined(*args, **kwargs):
        return (spell1(*args, **kwargs), spell2(*args, **kwargs))
    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def amplified(*args, **kwargs):
        return base_spell(*args, **kwargs) * multiplier
    return amplified


def conditional_caster(condition: callable, spell: callable) -> callable:
    def caster(*args, **kwargs):
        if condition(*args, **kwargs):
            return spell(*args, **kwargs)
        return "Spell fizzled"
    return caster


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs):
        return [spell(*args, **kwargs) for spell in spells]
    return sequence


if __name__ == '__main__':
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    print("Testing spell combiner...")
    combined = spell_combiner(fireball, heal)
    result = combined("Dragon")
    print(f"Combined spell result: {result[0]}, {result[1]}")

    print("Testing power amplifier...")

    def base_damage(power: int) -> int:
        return power

    mega = power_amplifier(base_damage, 3)
    print(f"Original: {base_damage(10)}, Amplified: {mega(10)}")

    print("Testing conditional caster...")

    def is_powerful(power: int) -> bool:
        return power >= 50

    def blast(power: int) -> str:
        return f"Blast deals {power} damage"

    caster = conditional_caster(is_powerful, blast)
    print(caster(80))
    print(caster(20))

    print("Testing spell sequence...")

    def shield(target: str) -> str:
        return f"Shield on {target}"

    sequence = spell_sequence([fireball, heal, shield])
    print(sequence("Mage"))
