import sys


def split_inventory(args: list) -> dict:
    inventory = {}
    for part in args:
        part = part.strip()
        if ":" not in part:
            print(f"Skipping invalid item: {part}")
            continue
        name, qty_str = part.split(":", 1)
        name = name.strip()
        qty_str = qty_str.strip()
        if name == "" or qty_str == "":
            print(f"Skipping invalid item: {part}")
            continue
        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Skipping invalid item: {part}")
            continue
        inventory[name] = qty
    return inventory


def count_inventory_items(inventory: dict) -> int:
    total = 0
    for key in inventory:
        total += inventory[key]
    return total


def perc_inventory(inventory: dict, total_items: int) -> None:
    sorted_items = sorted(inventory.items(), key=lambda x: x[1], reverse=True)
    for key, qty in sorted_items:
        percent = (qty / total_items) * 100.0 if total_items > 0 else 0.0
        unit = "unit" if qty == 1 else "units"
        print(f"{key}: {qty} {unit} ({percent:.1f}%)")


def find_max_item(inventory: dict) -> str:
    max_key = list(inventory.keys())[0]
    for key in inventory:
        if inventory[key] > inventory[max_key]:
            max_key = key
    return max_key


def find_min_item(inventory: dict) -> str:
    min_key = list(inventory.keys())[0]
    for key in inventory:
        if inventory[key] < inventory[min_key]:
            min_key = key
    return min_key


def categories_item(inventory: dict) -> tuple:
    scarce = {}
    moderate = {}
    for key in inventory:
        if inventory[key] < 5:
            scarce[key] = inventory[key]
        else:
            moderate[key] = inventory[key]
    return scarce, moderate


def search_restock(inventory: dict) -> dict:
    restock = {}
    for key in inventory:
        if inventory[key] <= 1:
            restock[key] = inventory[key]
    return restock


def is_present(inventory: dict, item: str) -> bool:
    if item in inventory and inventory[item] > 0:
        print(f"Sample lookup - '{item}' in inventory: True")
        return True
    print(f"Sample lookup - '{item}' in inventory: False")
    return False


def print_items(inventory: dict) -> None:
    for key in inventory:
        qty = inventory[key]
        unit = "unit" if qty == 1 else "units"
        print(f"{key}: {qty} {unit}")


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python3 ft_inventory_system.py item1:qty1 item2:qty2 ...")
        return

    inventory = split_inventory(sys.argv[1:])
    if len(inventory) == 0:
        print("No valid items in inventory.")
        return

    total_items = count_inventory_items(inventory)
    max_item = find_max_item(inventory)
    min_item = find_min_item(inventory)
    restock = search_restock(inventory)

    print("=== Inventory System Analysis ===")
    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inventory)}")

    print()
    print("=== Current Inventory ===")
    perc_inventory(inventory, total_items)

    print()
    print("=== Inventory Statistics ===")
    print(f"Most abundant: {max_item} ({inventory[max_item]} units)")
    print(f"Least abundant: {min_item} ({inventory[min_item]} units)")

    print()
    print("=== Item Categories ===")
    scarce, moderate = categories_item(inventory)
    print(f"Moderate: {moderate}")
    print(f"Scarce: {scarce}")

    print()
    print("=== Management Suggestions ===")
    if len(restock) == 0:
        print("All items are well stocked!")
    else:
        print("Restock needed: " + ", ".join(restock.keys()))

    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: " + ", ".join(inventory.keys()))
    print("Dictionary values: " + ", ".join(str(v) for v in inventory.values()))

    is_present(inventory, "sword")

    print()
    print("Why are dictionaries essential for game data?")
    print("How do nested dictionaries model complex relationships?")


if __name__ == "__main__":
    main()