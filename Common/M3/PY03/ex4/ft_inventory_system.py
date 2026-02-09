import sys

def ft_split(s, sep):
    result = []
    word = ""
    i = 0
    while i < len(s):
        if s[i] == sep:
            if word != "":
                result.append(word)
                word = ""
        else:
            word += s[i]
        i += 1
    if word != "":
        result.append(word)
    return result

if __name__ == "__main__":
    print("=== Inventory System Analysis ===")

    inv = dict()

    for arg in sys.argv[1:]:
        parts = ft_split(arg, ":")
        name = parts[0]
        qty = 0
        inv[name] = inv.get(name, 0) + qty

    total_items = 0
    for q in inv.values():
        total_items += q

    print(f"Total items in inventory: {total_items}")
    print(f"Unique item types: {len(inv)}")
    print("=== Current Inventory ===")
    for item, qty in inv.items():
        print(f"{item}: {qty}")
		