import re


def validate_ingredients(ingredients: str) -> str:
    try:
        res: list = []

        for i in ["fire", "water", "earth", "air"]:
            res += re.findall(i, ingredients)

        if len(res) > 0:
            return f"{ingredients} - VALID"
        else:
            return f"{ingredients} - INVALID"
    except Exception:
        return "ERROR: 'validator.py'"
