"""Module for managing player inventories and item transactions."""


def get_total_gold(loot: dict) -> int:
    """Calculate the total gold value of all items in the inventory."""
    total: int = 0
    for info in loot.values():
        total += info['qty'] * info['value']
    return total


def get_total_items(loot: dict) -> int:
    """Calculate the total quantity of all items in the inventory."""
    total: int = 0
    for info in loot.values():
        total += info['qty']
    return total


def get_rarest_items(loot: dict) -> str:
    """Identify and return a string of items with 'rare' rarity status."""
    total: str = ""
    for item, info in loot.items():
        if info['rarity'] == 'rare':
            if total != "":
                total += ", "
            total += item
    return total


def main() -> None:
    """
    Execute the player inventory system demonstration.

    Manages item data structures, performs transactions between players,
    and displays inventory analytics including value and rarity.
    """
    print("=== Player Inventory System ===")

    print("\n=== Alices's Inventory ===")
    alice_loot: dict = {
        'sword': {
            'type': 'weapon',
            'rarity': 'rare',
            'qty': 1,
            'value': 500
        },
        'potion': {
            'type': 'consumable',
            'rarity': 'common',
            'qty': 5,
            'value': 50
        },
        'shield': {
            'type': 'armor',
            'rarity': 'uncommon',
            'qty': 1,
            'value': 200
        }
    }

    bob_loot: dict = {
        'magic_ring': {
            'type': 'armor',
            'rarity': 'rare',
            'qty': 1,
            'value': 500
        }
    }

    total_value: int = get_total_gold(alice_loot)
    items_value: int = get_total_items(alice_loot)
    categories: dict = {}
    template: str = "{} ({}, {}): {}x @ {} gold each = {} gold"

    for item, info in alice_loot.items():
        value: int = info['qty'] * info['value']
        print(template.format(
            item, info.get('type'), info.get('rarity'),
            info.get('qty'), info.get('value'), value
        ))
        type: str = info.get('type')
        categories[type] = categories.get(type, 0) + info.get('qty')

    template: str = "Categories: {}({}), {}({}), {}({})"
    print(f"\nInventory value: {total_value} gold")
    print(f"Item count: {items_value} items")
    print(template.format(
        alice_loot['sword']['type'], categories.get('weapon', 0),
        alice_loot['potion']['type'], categories.get('consumable', 0),
        alice_loot['shield']['type'], categories.get('armor', 0)
    ))

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    item: str = 'potion'
    amount: int = 2

    alice_loot['potion']['qty'] -= amount

    if item not in bob_loot:
        bob_loot[item] = {
            'type': 'consumible',
            'rarity': 'common',
            'qty': 0,
            'value': 50
        }

    bob_loot[item]['qty'] += amount
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_loot[item]['qty']}")
    print(f"Bob potions: {bob_loot[item]['qty']}")

    print("\n=== Inventory Analytics ===")
    alice_gold: int = get_total_gold(alice_loot)
    bob_gold: int = get_total_gold(bob_loot)

    if alice_gold > bob_gold:
        print(f"Most valuable player: Alice ({alice_gold} gold)")
    else:
        print(f"Most valuable player: Bob ({bob_gold} gold)")

    alice_items: int = get_total_items(alice_loot)
    bob_items: int = get_total_items(bob_loot)

    if alice_items > bob_items:
        print(f"Most items: Alice ({alice_items} items)")
    else:
        print(f"Most items: Bob ({bob_items} items)")

    all_loots = {}
    all_loots.update(alice_loot)
    all_loots.update(bob_loot)
    rarest_items: str = get_rarest_items(all_loots)
    print(f"Rarest items: {rarest_items}")


if __name__ == "__main__":
    main()
