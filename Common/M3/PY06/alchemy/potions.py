def healing_potion() -> str:
    try:
        from .elements import create_fire, create_water
        return f"Healing potion brewed with {create_fire()}" +\
            f" and {create_water()}"
    except Exception:
        return "ERROR: potions.py -> healing_potion()"


def strength_potion() -> str:
    try:
        from .elements import create_earth, create_fire
        return f"Strength potion brewed with {create_earth()}" +\
            f"and {create_fire()}"
    except Exception:
        return "ERROR: potions.py -> strength_potion()"


def invisibility_potion() -> str:
    try:
        from .elements import create_air, create_water
        return f"Invisibility potion brewed with {create_air()}" +\
            f"and {create_water()}"
    except Exception:
        return "ERROR: potions.py -> invisibility_potion()"


def wisdom_potion() -> str:
    try:
        from .elements import (
            create_water,
            create_air,
            create_earth,
            create_fire
            )
        return "Wisdom potion brewed with all elements: " +\
            f"{create_water()}," +\
            f"{create_air()}," +\
            f"{create_fire()}," +\
            f"{create_earth()}"
    except Exception:
        return "ERROR: potions.py -> wisdom_potion()"
