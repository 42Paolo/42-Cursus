import functools
import operator
from collections.abc import Callable
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    """riduce la lista a un solo valore con l'operazione scelta"""
    if not spells:
        return 0
    ops = {
        'add': operator.add,
        'multiply': operator.mul,
        'max': max,
        'min': min,
    }
    if operation not in ops:
        raise ValueError(f"Unknown operation: {operation}")
    return functools.reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    """uso partial per pre-riempire power/element e returno i 3 incanti"""
    fire = functools.partial(base_enchantment, power=50, element='fire')
    ice = functools.partial(base_enchantment, power=50, element='ice')
    light = functools.partial(
        base_enchantment, power=50, element='lightning'
    )
    return {
        'fire_enchant': fire,
        'ice_enchant': ice,
        'lightning_enchant': light,
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """fibonacci ricorsivo, lru_cache si salva i risultati gia calcolati"""
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    """singledispatch sceglie la funzione giusta in base al tipo del valore"""
    @functools.singledispatch
    def dispatch(value):
        return "Unknown spell type"

    @dispatch.register(int)
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @dispatch.register(str)
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @dispatch.register(list)
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return dispatch


if __name__ == '__main__':
    spells = [10, 20, 30, 40]
    print("Testing spell reducer...")
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("Testing memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("Testing partial enchanter...")

    def base(target: str, power: int, element: str) -> str:
        return f"{element.capitalize()} enchant on {target} with power {power}"

    e = partial_enchanter(base)
    print(e['fire_enchant'](target='Sword'))
    print(e['ice_enchant'](target='Shield'))

    print("Testing spell dispatcher...")
    d = spell_dispatcher()
    print(d(42))
    print(d("fireball"))
    print(d([1, 2, 3]))
    print(d(3.14))
