from ast import Return
from re import split
import sys

def split_inventory(args):
	inventory = {}

	people = args[1:-1].split(", ")

	for person in people:
		name, age = person.split(":")
		inventory[name] = int(age)
	
	return inventory

def main():
	argc = len(sys.argv)
	if argc == 1:
		return 0

	args = sys.argv[1:]
	inventory = dict()
	inventory = split_inventory(args)


	#print(args)
	

if __name__ == "__main__":
	main()
