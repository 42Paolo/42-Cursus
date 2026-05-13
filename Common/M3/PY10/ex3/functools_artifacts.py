import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    make = functools.partial
    return {
        'fire_enchant': make(base_enchantment, power=50, element='fire'),
        'ice_enchant': make(base_enchantment, power=50, element='ice'),
        'lightning_enchant': make(
            base_enchantment, power=50, element='lightning'
        ),
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def dispatch(value):
        return f"Unknown spell type: {type(value)}"

    @dispatch.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage dealt"

    @dispatch.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value} applied"

    @dispatch.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells cast"

    return dispatch


if __name__ == '__main__':
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing partial enchanter...")

    def base(target: str, power: int, element: str) -> str:
        return f"{element.capitalize()} enchant on {target} with power {power}"

    enchants = partial_enchanter(base)
    print(enchants['fire_enchant'](target='Sword'))
    print(enchants['ice_enchant'](target='Shield'))

    print("Testing spell dispatcher...")
    dispatch = spell_dispatcher()
    print(dispatch(42))
    print(dispatch("Fireball"))
    print(dispatch([1, 2, 3]))
