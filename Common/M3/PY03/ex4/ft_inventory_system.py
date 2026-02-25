from ast import Return
from re import split
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

def main():
	argc = len(sys.argv)
	if argc == 1:
		return 0

	args = sys.argv[1:]
	inventory = split_inventory(args)
	total_items = count_inventory_items(inventory)

	print("=== Inventory System Analysis ===")
	print("Total items in inventory" )
	print("Unique item types: ", len(inventory))
	
	

	#print(args)
	

if __name__ == "__main__":
	main()
