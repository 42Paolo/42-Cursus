def record_spell(spell_name: str, ingredients: str) -> str:
    try:
        from .validator import validate_ingredients as valing
        result = valing(ingredients=ingredients)

        if "- VALID" in result:
            return f"Spell recorded: {spell_name} ({result})"
        else:
            return f"Spell rejected: {spell_name} ({result})"

    except Exception:
        return "ERROR: 'record_spell.py'"
