"""
This module demonstrates functional programming in Python using lambdas.
It provides utilities to sort, filter, transform, and analyze magical
mages and spells. Each function showcases concise, functional-style
data manipulation.
"""

from typing import TypedDict


class Mage(TypedDict):
    name: str
    power: int | float
    element: str


wordlist: list[str] = [
        'fireball',
        'heal',
        'shield',
        'frostbolt',
        'arcane blast'
    ]

Dictlist: list[Mage] = [
        {'name': 'Aeris', 'power': 95, 'element': 'air'},
        {'name': 'Pyra', 'power': 88, 'element': 'fire'},
        {'name': 'Terra', 'power': 72, 'element': 'earth'},
        {'name': 'Hydra', 'power': 65, 'element': 'water'},
        {'name': 'Lux', 'power': 80, 'element': 'light'}
    ]


def artifact_sorter(artifacts: list[Mage]) -> list[Mage]:
    """
    Sorts a list of artifacts by their 'power' value in descending order.
    """
    return sorted(artifacts, key=lambda artifact: artifact['power'],
                  reverse=True)


def power_filter(mages: list[Mage], min_power: int) -> list[Mage]:
    """
    Filters mages whose 'power' is greater than or equal to min_power.
    """
    return list(filter(lambda mage: mage['power'] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    """
    Transforms spell names by adding '* ' prefix and ' *' suffix.
    """
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[Mage]) -> dict[str, int | float]:
    """
    Calculates statistics for a list of mages: max, min, and average power.
    """
    if not mages:
        return {'max_power': 0, 'min_power': 0, 'avg_power': 0.0}

    powers = [p for p in map(lambda mage: mage['power'], mages)]
    return {
            "max_power": max(powers),
            "min_power": min(powers),
            "avg_power": round(sum(powers) / len(mages), 2)
    }


def main():
    new_artifact: list[Mage] = artifact_sorter(Dictlist)

    print("Testing artifact sorter...")
    template = "{} ({}) comes before {} ({})"
    print(template.format(new_artifact[0]['name'], new_artifact[0]['power'],
                          new_artifact[1]['name'], new_artifact[1]['power']))

    new_power: list[Mage] = power_filter(Dictlist, 75)

    print("\nTesting power filter...")
    print(", ".join(str(power['power']) for power in new_power))

    new_spell_transformer: list[str] = spell_transformer(wordlist)

    print("\nTesting spell transformer...")
    print(" ".join(new_spell_transformer))

    new_mage: dict[str, int | float] = mage_stats(Dictlist)

    print("\nTesting mage stats...")
    print(new_mage)


if __name__ == "__main__":
    main()
