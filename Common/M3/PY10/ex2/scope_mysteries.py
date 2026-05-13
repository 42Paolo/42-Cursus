def mage_counter() -> callable:
    count = 0

    def counter() -> int:
        nonlocal count
        count += 1
        return count

    return counter


def spell_accumulator(initial_power: int) -> callable:
    total = initial_power

    def accumulate(amount: int) -> int:
        nonlocal total
        total += amount
        return total

    return accumulate


def enchantment_factory(enchantment_type: str) -> callable:
    def enchant(item: str) -> str:
        return f"{enchantment_type} {item}"

    return enchant


def memory_vault() -> dict[str, callable]:
    storage: dict = {}

    def store(key: str, value) -> None:
        storage[key] = value

    def recall(key: str):
        return storage.get(key, "Memory not found")

    return {'store': store, 'recall': recall}


if __name__ == '__main__':
    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("Testing enchantment factory...")
    flame = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flame("Sword"))
    print(frozen("Shield"))

    print("Testing spell accumulator...")
    acc = spell_accumulator(100)
    print(f"After +50: {acc(50)}")
    print(f"After +30: {acc(30)}")

    print("Testing memory vault...")
    vault = memory_vault()
    vault['store']('spell', 'Fireball')
    print(vault['recall']('spell'))
    print(vault['recall']('missing'))
