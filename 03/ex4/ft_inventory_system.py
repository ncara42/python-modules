"""Docstrings"""


def get_total_gold(loot: dict) -> int:
    total = 0
    for info in loot.values():
        total += info['qty'] * info['value']
    return total


def get_total_items(loot: dict) -> int:
    total = 0
    for info in loot.values():
        total += info['qty']
    return total


def get_rarest_items(loot: dict) -> str:
    total = ""
    for item, info in loot.items():
        if info['rarity'] == 'rare':
            if total != "":
                total += ", "
            total += item
    return total


def main() -> None:

    print("=== Player Inventory System ===")

    print("\n=== Alices's Inventory")
    alice_loot = {
        'sword': {'type': 'weapon', 'rarity': 'rare', 'qty': 1, 'value': 500},
        'potion': {'type': 'consumable', 'rarity': 'common', 'qty': 5, 'value': 50},
        'shield': {'type': 'armor', 'rarity': 'uncommon', 'qty': 1, 'value': 200}
    }

    bob_loot = {
        'sword': {'type': 'weapon', 'rarity': 'rare', 'qty': 1, 'value': 500},
        'potion': {'type': 'consumable', 'rarity': 'common', 'qty': 0, 'value': 50},
        'shield': {'type': 'armor', 'rarity': 'uncommon', 'qty': 1, 'value': 200},
        'magic_ring': {'type': 'armor', 'rarity': 'rare', 'qty': 1, 'value': 500}
    }

    total_value = get_total_gold(alice_loot)
    items_value = get_total_items(alice_loot)
    categories = {}

    for item, info in alice_loot.items():
        value = info['qty'] * info['value']
        print(f"{item}: ({info.get('type')}, {info.get('rarity')}): {info.get('qty')}x @ {info.get('value')} gold each = {value} gold")
        type = info.get('type')
        categories[type] = categories.get(type, 0) + info.get('qty')
    
    print(f"\nInventory value: {total_value}")
    print(f"Item count: {items_value}")
    print(f"Categories: {alice_loot['sword']['type']}({categories.get('weapon', 0)}), " 
          f"{alice_loot['potion']['type']}({categories.get('consumable', 0)}), "
          f"{alice_loot['shield']['type']}({categories.get('armor', 0)})")

    print("\n=== Transaction: Alice gives Bob 2 potions ===")
    item = 'potion'
    amount = 2

    alice_loot['potion']['qty'] -= amount

    if item not in bob_loot:
        bob_loot[item] = {'type': 'consumible', 'rarity': 'common', 'qty': 0, 'value': 50}
    bob_loot[item]['qty'] += amount
    print("Transaction successful!")

    print("\n=== Updated Inventories ===")
    print(f"Alice potions: {alice_loot[item]['qty']}")
    print(f"Bob potions: {bob_loot[item]['qty']}")

    print("\n=== Inventory Analytics ===")
    alice_gold = get_total_gold(alice_loot)
    bob_gold = get_total_gold(bob_loot)

    if alice_gold > bob_gold:
        print(f"Most valuable player: Alice ({alice_gold})")
    else:
        print(f"Most valuable player: Bob ({bob_gold})")

    alice_items = get_total_items(alice_loot)
    bob_items = get_total_items(bob_loot)

    if alice_items > bob_items:
         print(f"Most items: Alice ({alice_items})")
    else:
        print(f"Most items: Bob ({bob_items})")
    
    rarest_items = get_rarest_items(bob_loot)
    print(f"Rarest items: {rarest_items}")


if __name__ == "__main__":
    main()
