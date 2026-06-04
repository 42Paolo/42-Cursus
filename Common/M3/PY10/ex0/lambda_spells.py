
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    """Ordina gli artefatti per potere."""
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    """filtro solo per i maze hanno forza+ rispetto min"""
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """aggiunta asterischi per incantesimo"""
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:

    """max/min/media power, uso map"""
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}
    total = sum(map(lambda m: m['power'], mages))
    return {
        'max_power': max(mages, key=lambda m: m['power'])['power'],
        'min_power': min(mages, key=lambda m: m['power'])['power'],
        'avg_power': round(total / len(mages), 2)
    }


if __name__ == '__main__':
    artifacts = [
        {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'},
        {'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
        {'name': 'Shadow Blade', 'power': 78, 'type': 'weapon'},
    ]
    ordered = artifact_sorter(artifacts)
    print("Testing artifact sorter...")
    a = ordered[0]
    b = ordered[1]
    name1 = a['name']
    pow1 = a['power']
    name2 = b['name']
    pow2 = b['power']
    print(f"{name1} ({pow1} power) comes before {name2} ({pow2} power)")

    print("Testing spell transformer...")
    print(*spell_transformer(['fireball', 'heal', 'shield']))

    mages = [
        {'name': 'Alex', 'power': 70, 'element': 'fire'},
        {'name': 'Jordan', 'power': 90, 'element': 'ice'},
        {'name': 'Riley', 'power': 55, 'element': 'wind'},
    ]
    print("Testing power filter (min 65)...")
    strong = power_filter(mages, 65)
    print([m['name'] for m in strong])

    print("Testing mage stats...")
    s = mage_stats(mages)
    mx = s['max_power']
    mn = s['min_power']
    av = s['avg_power']
    print(f"Max: {mx}, Min: {mn}, Avg: {av}")
