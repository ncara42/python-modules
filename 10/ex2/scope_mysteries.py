from typing import Callable, Any


def mage_counter() -> Callable[[], int]:
    counter = 0

    def incrementer():
        nonlocal counter
        counter += 1
        return counter
    return incrementer


def spell_accumulator(initial_power: int) -> Callable[[], int]:
    step = initial_power
    total = 0

    def incrementer():
        nonlocal total
        total += step
        return total
    return incrementer


def enchantment_factory(enchantment_type: str) -> Callable[[str], str]:

    def concatenate(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return concatenate


def memory_vault() -> dict[str, Callable[..., Any]]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> Any:
        return memory.get(key, "Memory not found")
    return {'store': store, 'recall': recall}


def main() -> None:
    print("Testing mage counter...")
    mage = mage_counter()

    for i in range(1, 4):
        print(f"Call {i}: {mage()}")

    print("\nTesting mage counter...")
    spell = spell_accumulator(15)

    for i in range(1, 4):
        print(f"Call {i}: {spell()}")

    print("\nTesting enchantment_factory...")
    enchanter = enchantment_factory("Flaming")
    print(enchanter("Sword"))
    enchanter = enchantment_factory("Frozen")
    print(enchanter("Sword"))

    print("\nTesting memory_vault...")
    vault = memory_vault()
    print(vault['store']("spell", "Fireball"))
    print(vault['recall']("spell"))


if __name__ == "__main__":
    main()
