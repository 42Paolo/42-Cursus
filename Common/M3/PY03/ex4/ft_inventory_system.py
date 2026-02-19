import sys


def parse_inventory(args: list[str]) -> dict[str, int]:
    inventory: dict[str, int] = dict()
    for arg in args:
        try:
            parts = arg.split(":")
            item = parts[0]
            qty = int(parts[1])
            inventory.update({item: qty})
        except (ValueError, IndexError):
            print(f"Skipping invalid item: {arg}")
    return inventory


def main() -> None:
    args = sys.argv[1:]

    if len(args) == 0:
        print("Usage: python3 ft_inventory_system.py"
              " item1:qty1 item2:qty2 ...")
        return

    inventory = parse_inventory(args)

    if len(inventory) == 0:
        print("No valid items in inventory.")
        return

    total_items = sum(inventory.values())
    unique_types = len(inventory.keys())

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {unique_types}")

    print()
    print("=== Current Inventory ===")
    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for item, qty in sorted_items:
        percent = (qty / total_items) * 100
        unit_word = "units" if qty > 1 else "unit"
        print(f"{item}: {qty} {unit_word} ({percent:.1f}%)")

    most_abundant = max(inventory.keys(), key=lambda k: inventory[k])
    least_abundant = min(inventory.keys(), key=lambda k: inventory[k])

    print()
    print("=== Inventory Statistics ===")
    most_qty = inventory.get(most_abundant, 0)
    least_qty = inventory.get(least_abundant, 0)
    most_unit = "units" if most_qty > 1 else "unit"
    least_unit = "units" if least_qty > 1 else "unit"
    print(f"Most abundant: {most_abundant} ({most_qty} {most_unit})")
    print(f"Least abundant: {least_abundant} ({least_qty} {least_unit})")

    print()
    print("=== Item Categories ===")
    moderate: dict[str, int] = dict()
    scarce: dict[str, int] = dict()
    for item, qty in inventory.items():
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print()
    print("=== Management Suggestions ===")
    restock = [item for item, qty in inventory.items() if qty <= 1]
    if restock:
        print(f"Restock needed: {', '.join(restock)}")
    else:
        print("All items are well stocked!")

    print()
    print("=== Dictionary Properties Demo ===")
    print(f"Dictionary keys: {', '.join(inventory.keys())}")
    vals = ', '.join(str(v) for v in inventory.values())
    print(f"Dictionary values: {vals}")
    sword_check = 'sword' in inventory
    print(f"Sample lookup - 'sword' in inventory: {sword_check}")


main()
