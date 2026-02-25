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

def main():
	argc = len(sys.argv)
	if argc == 1:
		return 0

	args = sys.argv[1:]
	inventory = split_inventory(args)
	total_items = count_inventory_items(inventory)
	max = search_max(inventory)
	min = search_min(inventory)
	print("=== Inventory System Analysis ===")
	print("Total items in inventory" )
	print("Unique item types: ", len(inventory))
	print("\n=== Current Inventory ===")
	perc_inventory(inventory, total_items)
	print("\n=== Inventory Statistics ===")
	print(f"Most abundant: {max} ({inventory[max]} units)")
	print(f"Most abundant: {min} ({inventory[min]} units)")
	

	#print(args)
	

if __name__ == "__main__":
	main()
