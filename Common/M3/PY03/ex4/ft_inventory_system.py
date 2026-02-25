import sys


def split_inventory(arg_str: str) -> dict[str, int]:
    inventory: dict[str, int] = {}
    entries = arg_str.split(",")
    i = 0
    while i < len(entries):
        part = entries[i].strip()
        if part == "":
            i += 1
            continue
        if ":" not in part:
            print(f"Skipping invalid item: {part}")
            i += 1
            continue
        name, qty_str = part.split(":", 1)
        name = name.strip()
        qty_str = qty_str.strip()
        if name == "" or qty_str == "":
            print(f"Skipping invalid item: {part}")
            i += 1
            continue
        try:
            qty = int(qty_str)
        except ValueError:
            print(f"Skipping invalid item: {part}")
            i += 1
            continue
        inventory[name] = qty
        i += 1
    return inventory


def count_inventory_items(inventory: dict[str, int]) -> int:
    total = 0
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        total = total + inventory[key]
        i += 1
    return total


def perc_inventory(inventory: dict[str, int], total_items: int) -> None:
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        qty = inventory[key]
        percent = 0.0
        if total_items > 0:
            percent = (qty / total_items) * 100.0
        unit = "unit"
        if qty != 1:
            unit = "units"
        print(f"{key}: {qty} {unit} ({percent:.1f}%)")
        i += 1


def find_max_item(inventory: dict[str, int]) -> str:
    keys = list(inventory.keys())
    max_key = keys[0]
    i = 1
    while i < len(keys):
        key = keys[i]
        if inventory[key] > inventory[max_key]:
            max_key = key
        i += 1
    return max_key


def find_min_item(inventory: dict[str, int]) -> str:
    keys = list(inventory.keys())
    min_key = keys[0]
    i = 1
    while i < len(keys):
        key = keys[i]
        if inventory[key] < inventory[min_key]:
            min_key = key
        i += 1
    return min_key


def categories_item(
    inventory: dict[str, int]
) -> tuple[dict[str, int], dict[str, int]]:
    moderate: dict[str, int] = {}
    scarce: dict[str, int] = {}
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        qty = inventory[key]
        if qty < 5:
            scarce[key] = qty
        else:
            moderate[key] = qty
        i += 1
    return scarce, moderate


def search_restock(inventory: dict[str, int]) -> dict[str, int]:
    restock: dict[str, int] = {}
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        qty = inventory[key]
        if qty <= 1:
            restock[key] = qty
        i += 1
    return restock


def is_present(inventory: dict[str, int], item: str) -> bool:
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        if key == item and inventory[key] > 0:
            print(f"Sample lookup - '{item}' in inventory: True")
            return True
        i += 1
    print(f"Sample lookup - '{item}' in inventory: False")
    return False


def print_items(inventory: dict[str, int]) -> None:
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        qty = inventory[key]
        unit = "unit"
        if qty != 1:
            unit = "units"
        print(f"{key}: {qty} {unit}")
        i += 1


def main() -> None:
    if len(sys.argv) != 2:
        print(
            "Usage: python3 ft_inventory_system.py "
            "\"item1:qty1, item2:qty2, ...\""
        )
        return

    inventory = split_inventory(sys.argv[1])
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
    print("Moderate:")
    print_items(moderate)
    print("Scarce:")
    print_items(scarce)

    print()
    print("=== Management Suggestions ===")
    if len(restock) == 0:
        print("All items are well stocked!")
    else:
        print("Restock needed: ", end="")
        names = list(restock.keys())
        i = 0
        while i < len(names):
            if i > 0:
                print(", ", end="")
            print(names[i], end="")
            i += 1
        print()

    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys: ", end="")
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        if i > 0:
            print(", ", end="")
        print(keys[i], end="")
        i += 1
    print()
    print("Dictionary values: ", end="")
    values = list(inventory.values())
    i = 0
    while i < len(values):
        if i > 0:
            print(", ", end="")
        print(values[i], end="")
        i += 1
    print()

    is_present(inventory, "sword")


if __name__ == "__main__":
    main()

from ast import Return
from re import split
from select import kevent
import sys

def split_inventory(args):
	inventory = {}

	people = args[1:-1].split(", ")

	for person in people:
		name, qty = person.split(":")
		inventory[name] = int(qty)

	return inventory

def count_inventory_items(inventory):
    total = 0
    keys = list(inventory.keys())
    i = 0
    while i < len(keys):
        key = keys[i]
        total = total + inventory[key]
        i = i + 1
    return total

def perc_inventory(inventory, tot_items):
	keys = list(inventory.keys())
	i = 0
	while i < len(keys):
		key = keys[i]
		perc = (inventory[key] / tot_items) * 100
		print(f"{key}: {inventory[key]} units ({perc}%)")
		i = i + 1

def search_max(inventory):
	keys = list(inventory.keys())
	i = 0
	max = inventory[0]
	while i < len(keys):
		key = keys[i]
		if inventory[key] > max:
			max = key
		i = i + 1 
	return max

def search_min(inventory):
	keys = list(inventory.keys())
	i = 0
	min = inventory[0]
	while i < len(keys):
		key = keys[i]
		if inventory[key] < min:
			min = key 
		i = i + 1	
	return min

def categories_item(inventory):
    mod_inv = dict()
    scar_inv = dict()
    for key in inventory:
        if inventory[key] < 5:
            scar_inv[key] = inventory[key]
        else:
            mod_inv[key] = inventory[key]
    return scar_inv, mod_inv

def search_restock(inventory):
	rest_inv = dict()
	for key in inventory:
		if inventory[key] <= 1:
			rest_inv[key] = inventory[key]
	return rest_inv

def is_present(inventory, gun):
	keys = inventory.keys()
	i = 0
	while i < len(keys):
		key = keys[i]
		if key == gun and inventory[key] > 0:
			print(f"Sample lookup - '{gun}' in inventory: True")
			return
		i = i + 1
	print(f"Sample lookup - '{gun}' in inventory: False")
	return False

def main():
	argc = len(sys.argv)
	if argc == 1:
		return 0

	args = sys.argv[1:]
	inventory = split_inventory(args)
	total_items = count_inventory_items(inventory)
	max = search_max(inventory)
	min = search_min(inventory)
	rest_inv = search_restock(inventory)
	print("=== Inventory System Analysis ===")
	print("Total items in inventory" )
	print("Unique item types: ", len(inventory))
	print("\n=== Current Inventory ===")
	perc_inventory(inventory, total_items)
	print("\n=== Inventory Statistics ===")
	print(f"Most abundant: {max} ({inventory[max]} units)")
	print(f"Most abundant: {min} ({inventory[min]} units)")
	print("=== Item Categories ===")
	scars, mods = categories_item(inventory)
	print(f"Moderate: {mods}")
	print(f"Scarce: {scars}")
	print("\n=== Management Suggestions ===")
	print("Restock needed: ", end="")
	print(f", ".join(rest_inv.keys()))
	print("\n=== Dictionary Properties Demo ===")
	print(f"Dictionary keys: ", end = "")
	print(f", ".join(inventory.keys()))
	print(f"Dictionary values: ", end = "")
	print(", ".join(str(qty) for qty in inventory.values()))
	is_present(inventory, "sword")
	

if __name__ == "__main__":
	main()
