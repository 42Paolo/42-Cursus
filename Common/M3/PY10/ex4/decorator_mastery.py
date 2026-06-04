import functools
import time
from collections.abc import Callable


def spell_timer(func: Callable) -> Callable:
    """decoratore che cronometra quanto ci mette la funzione"""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kwargs)
        elapsed = time.time() - start
        print(f"Spell completed in {elapsed:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    """decoratore con parametro, lascia passare solo se power >= min"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if 'power' in kwargs:
                power = kwargs['power']
            elif args:
                power = args[-1]
            else:
                power = 0
            if power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    """decoratore che riprova finche non va o finisce i tentativi"""
    def decorator(func: Callable) -> Callable:
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print(
                            f"Spell failed, retrying..."
                            f" (attempt {attempt}/{max_attempts})"
                        )
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """controlla che il nome sia lungo almeno 3 e solo lettere/spazi"""
        if len(name) < 3:
            return False
        for c in name:
            if not c.isalpha() and not c.isspace():
                return False
        return True

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """lancia lo spell, ma il decoratore blocca se power troppo basso"""
        return f"Successfully cast {spell_name} with {power} power"


if __name__ == '__main__':
    @spell_timer
    def fireball():
        time.sleep(0.1)
        return "Fireball cast!"

    print("Testing spell timer...")
    res = fireball()
    print(f"Result: {res}")

    print("Testing retrying spell...")

    @retry_spell(max_attempts=3)
    def always_fails() -> str:
        raise RuntimeError("Spell fizzled")

    print(always_fails())

    @retry_spell(max_attempts=3)
    def waaaaaagh_spell() -> str:
        return "Waaaaaagh spelled !"

    print(waaaaaagh_spell())

    print("Testing MageGuild...")
    g = MageGuild()
    print(MageGuild.validate_mage_name("Merlin"))
    print(MageGuild.validate_mage_name("X2"))
    print(g.cast_spell("Lightning", 15))
    print(g.cast_spell("Lightning", 5))
