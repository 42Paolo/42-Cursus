import sys


def main() -> None:
    print("=== Inventory System Analysis ===")

    if len(sys.argv) == 1:
        print("No inventory provided.")
        print(
            "Usage: python3 ft_inventory_system.py "
            "item1:qty1 item2:qty2 ..."
        )
        return

    inventory = {}
    for arg in sys.argv[1:]:
        try:
            parts = arg.split(":")
            name = parts[0]
            qty = int(parts[1])
            if name in inventory:
                inventory[name] += qty
            else:
                inventory[name] = qty
        except (ValueError, IndexError):
            print(f"Warning: invalid format '{arg}'")

    total = sum(inventory.values())
    print(f"Total items in inventory: {total}")
    print(f"Unique item types: {len(inventory)}")

    print()
    print("=== Current Inventory ===")
    sorted_inv = dict(
        sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    )
    for item, qty in sorted_inv.items():
        label = "unit" if qty == 1 else "units"
        print(f"{item}: {qty} {label} ({qty / total * 100:.1f}%)")

    print()
    print("=== Inventory Statistics ===")
    most = max(inventory, key=lambda x: inventory[x])
    least = min(inventory, key=lambda x: inventory[x])
    ml = "unit" if inventory[most] == 1 else "units"
    ll = "unit" if inventory[least] == 1 else "units"
    print(f"Most abundant: {most} ({inventory[most]} {ml})")
    print(f"Least abundant: {least} ({inventory[least]} {ll})")

    print()
    print("=== Item Categories ===")
    moderate = {}
    scarce = {}
    for item, qty in inventory.items():
        if qty >= 4:
            moderate[item] = qty
        else:
            scarce[item] = qty
    if moderate:
        print(f"Moderate: {moderate}")
    if scarce:
        print(f"Scarce: {scarce}")

    print()
    print("=== Management Suggestions ===")
    restock = [item for item, qty in inventory.items() if qty <= 1]
    if restock:
        print(f"Restock needed: {', '.join(restock)}")

    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    vals = ', '.join(str(v) for v in inventory.values())
    print(f"Dictionary values: {vals}")
    first = list(inventory.keys())[0]
    print(f"Sample lookup - '{first}' in inventory: {first in inventory}")


main()
