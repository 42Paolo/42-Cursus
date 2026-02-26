import sys


def split_inventory(args: list) -> dict:
	inventory = dict()
	for part in args:
		if ":" not in part:
			print(f"Skipping invalid item: {part}")
			continue
		sep = part.index(":")
		name = part[:sep]
		qty_str = part[sep + 1:]
		if name == "" or qty_str == "":
			print(f"Skipping invalid item: {part}")
			continue
		qty = 0
		valid = True
		for ch in qty_str:
			if ch < "0" or ch > "9":
				valid = False
				break
			qty = qty * 10 + (ord(ch) - ord("0"))
		if not valid:
			print(f"Skipping invalid item: {part}")
			continue
		inventory.update({name: qty})
	return inventory


def count_inventory_items(inventory: dict) -> int:
	total = 0
	for key in inventory.keys():
		total += inventory.get(key, 0)
	return total


def perc_inventory(inventory: dict, total_items: int) -> None:
	pairs = list(inventory.items())
	i = 0
	while i < len(pairs):
		j = i + 1
		while j < len(pairs):
			if pairs[j][1] > pairs[i][1]:
				tmp = pairs[i]
				pairs[i] = pairs[j]
				pairs[j] = tmp
			j += 1
		i += 1
	for key, qty in pairs:
		if total_items > 0:
			percent = (qty / total_items) * 100.0
		else:
			percent = 0.0
		if qty == 1:
			unit = "unit"
		else:
			unit = "units"
		print(f"{key}: {qty} {unit} ({percent:.1f}%)")


def find_max_item(inventory: dict) -> str:
	best_key = ""
	best_val = -1
	for key in inventory.keys():
		val = inventory.get(key, 0)
		if val > best_val:
			best_val = val
			best_key = key
	return best_key


def find_min_item(inventory: dict) -> str:
	worst_key = ""
	worst_val = -1
	for key in inventory.keys():
		val = inventory.get(key, 0)
		if worst_val == -1 or val < worst_val:
			worst_val = val
			worst_key = key
	return worst_key


def categories_item(inventory: dict) -> tuple:
	scarce = dict()
	moderate = dict()
	for key in inventory.keys():
		val = inventory.get(key, 0)
		if val < 5:
			scarce.update({key: val})
		else:
			moderate.update({key: val})
	return scarce, moderate


def search_restock(inventory: dict) -> dict:
	restock = dict()
	for key in inventory.keys():
		if inventory.get(key, 0) <= 1:
			restock.update({key: inventory.get(key, 0)})
	return restock


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
	max_qty = inventory.get(max_item, 0)
	min_qty = inventory.get(min_item, 0)
	print(f"Most abundant: {max_item} ({max_qty} units)")
	if min_qty == 1:
		print(f"Least abundant: {min_item} ({min_qty} unit)")
	else:
		print(f"Least abundant: {min_item} ({min_qty} units)")

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
		restock_str = ""
		first = True
		for key in restock.keys():
			if not first:
				restock_str += ", "
			restock_str += key
			first = False
		print(f"Restock needed: {restock_str}")

	print()
	print("=== Dictionary Properties Demo ===")
	keys_str = ""
	first = True
	for key in inventory.keys():
		if not first:
			keys_str += ", "
		keys_str += key
		first = False
	print(f"Dictionary keys: {keys_str}")

	vals_str = ""
	first = True
	for val in inventory.values():
		if not first:
			vals_str += ", "
		vals_str += str(val) if False else f"{val}"
		first = False
	print(f"Dictionary values: {vals_str}")

	item = "sword"
	if inventory.get(item, 0) > 0:
		print(f"Sample lookup - '{item}' in inventory: True")
	else:
		print(f"Sample lookup - '{item}' in inventory: False")


if __name__ == "__main__":
	main()
