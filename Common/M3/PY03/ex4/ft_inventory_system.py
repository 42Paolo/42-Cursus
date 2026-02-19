import sys


def parse_inventory(args):
    inv = dict()
    i = 0
    while i < len(args):
        try:
            parts = args[i].split(":")
            item = parts[0]
            qty = int(parts[1])
            inv[item] = qty
        except (ValueError, IndexError):
            print("Skipping invalid item:", args[i])
        i = i + 1
    return inv


def main():
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: python3 ft_inventory_system.py item1:qty1 item2:qty2 ...")
        return
    inv = parse_inventory(args)
    if len(inv) == 0:
        print("No valid items in inventory.")
        return
    total_items = 0
    keys_list = list(inv.keys())
    k = 0
    while k < len(keys_list):
        total_items = total_items + inv[keys_list[k]]
        k = k + 1
    unique_types = len(inv.keys())
    print("=== Inventory System Analysis ===")
    print("Total items in inventory:", total_items)
    print("Unique item types:", unique_types)
    print()
    print("=== Current Inventory ===")
    items_list = list(inv.items())
    i = 0
    while i < len(items_list):
        j = i + 1
        while j < len(items_list):
            if items_list[j][1] > items_list[i][1]:
                tmp = items_list[i]
                items_list[i] = items_list[j]
                items_list[j] = tmp
            j = j + 1
        i = i + 1
    idx = 0
    while idx < len(items_list):
        item = items_list[idx][0]
        qty = items_list[idx][1]
        percent = (qty / total_items) * 100
        if qty > 1:
            unit_word = "units"
        else:
            unit_word = "unit"
        print(item, ":", qty, unit_word, "(", round(percent, 1), "%)")
        idx = idx + 1
    most_abundant = keys_list[0]
    least_abundant = keys_list[0]
    m = 0
    while m < len(keys_list):
        if inv[keys_list[m]] > inv[most_abundant]:
            most_abundant = keys_list[m]
        if inv[keys_list[m]] < inv[least_abundant]:
            least_abundant = keys_list[m]
        m = m + 1
    print()
    print("=== Inventory Statistics ===")
    most_qty = inv.get(most_abundant, 0)
    least_qty = inv.get(least_abundant, 0)
    if most_qty > 1:
        most_unit = "units"
    else:
        most_unit = "unit"
    if least_qty > 1:
        least_unit = "units"
    else:
        least_unit = "unit"
    print("Most abundant:", most_abundant, "(", most_qty, most_unit, ")")
    print("Least abundant:", least_abundant, "(", least_qty, least_unit, ")")
    print()
    print("=== Item Categories ===")
    moderate = dict()
    scarce = dict()
    it = 0
    while it < len(keys_list):
        item = keys_list[it]
        qty = inv[item]
        if qty >= 5:
            moderate[item] = qty
        else:
            scarce[item] = qty
        it = it + 1
    print("Moderate:", moderate)
    print("Scarce:", scarce)
    print()
    print("=== Management Suggestions ===")
    restock = []
    r = 0
    while r < len(keys_list):
        if inv[keys_list[r]] <= 1:
            restock.append(keys_list[r])
        r = r + 1
    if len(restock) > 0:
        print("Restock needed:", ", ".join(restock))
    else:
        print("All items are well stocked!")
    print()
    print("=== Dictionary Properties Demo ===")
    print("Dictionary keys:", ", ".join(inv.keys()))
    vals_list = list(inv.values())
    v_str = ""
    v = 0
    while v < len(vals_list):
        if v > 0:
            v_str = v_str + ", "
        v_str = v_str + str(vals_list[v])
        v = v + 1
    print("Dictionary values:", v_str)
    sword_check = 'sword' in inv
    print("Sample lookup - 'sword' in inventory:", sword_check)


main()
