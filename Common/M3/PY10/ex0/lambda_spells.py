def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda a: a['power'], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda m: m['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda s: f"* {s} *", spells))


def mage_stats(mages: list[dict]) -> dict:
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
    sorted_artifacts = artifact_sorter(artifacts)
    first = sorted_artifacts[0]
    second = sorted_artifacts[1]
    print("Testing artifact sorter...")
    print(
        f"{first['name']} ({first['power']} power)"
        f" comes before"
        f" {second['name']} ({second['power']} power)"
    )

    print("Testing spell transformer...")
    print(*spell_transformer(['fireball', 'heal', 'shield']))

    mages = [
        {'name': 'Alex', 'power': 70, 'element': 'fire'},
        {'name': 'Jordan', 'power': 90, 'element': 'ice'},
        {'name': 'Riley', 'power': 55, 'element': 'wind'},
    ]
    print("Testing power filter (min 65)...")
    filtered = power_filter(mages, 65)
    print([m['name'] for m in filtered])

    print("Testing mage stats...")
    stats = mage_stats(mages)
    print(
        f"Max: {stats['max_power']},"
        f" Min: {stats['min_power']},"
        f" Avg: {stats['avg_power']}"
    )
