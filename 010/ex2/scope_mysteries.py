from typing import Callable

def mage_counter(counter: int = 0) -> Callable[[], int]:
    def incrementer():
        nonlocal counter
        counter += 1
        return counter
    return incrementer


def spell_accumulator(initial_power: int) -> callable:
    pass


def enchantment_factory(enchantment_type: str) -> callable:
    pass


def memory_vault() -> dict[str, callable]:
    pass


def main() -> None:
    print("Testing mage counter...")
    func = mage_counter()

    for i in range(1, 4):
        print(f"Call {i}: {func()}")


    pass


if __name__ == "__main__":
    main()