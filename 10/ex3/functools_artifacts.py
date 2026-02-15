from typing import Callable, Any
from functools import reduce, partial, lru_cache, singledispatch
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    ops: dict[str, Any] = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }
    if operation not in ops:
        raise ValueError(f"Unsopported operation: {operation}")
    return reduce(ops[operation], spells)


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]) \
                      -> dict[str, Callable[[str], str]]:
    fire_enchant = partial(base_enchantment, 40, 'fire')
    ice_enchant = partial(base_enchantment, 50, 'ice')
    lightning_enchant = partial(base_enchantment, 50, 'lightning')
    return {
        'fire_enchant': fire_enchant,
        'ice_enchant': ice_enchant,
        'lightning_enchant': lightning_enchant
    }


def memoized_fibonacci(n: int) -> int:
    @lru_cache(maxsize=None)
    def fib(k: int) -> int:
        if k < 2:
            return k
        return fib(k-1) + fib(k-2)
    return fib(n)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def cast(spell):
        raise TypeError(f"Unsupported spell type: {type(spell).__name__}")

    @cast.register(int)
    def _(spell: int) -> str:
        return f"Damage spell cast! Damage: {spell}"

    @cast.register(str)
    def _(spell: str) -> str:
        return f"Enchantment spell cast! Enchantment: {spell}"

    @cast.register(list)
    def _(spell: list[Any]) -> str:
        return f"Multi-cast spell! Spells: {', '.join(map(str, spell))}"

    return cast


def main():
    spells = [2, 3, 5, 7]
    print("Testing spell reducer...")
    print("Sum:", spell_reducer(spells, "add"))
    print("Product:", spell_reducer(spells, "multiply"))
    print("Max:", spell_reducer(spells, "max"))
    print("Min:", spell_reducer(spells, "min"))

    def base_enchantment(power: int, element: str, target: str) -> str:
        return f"{element.title()} {target} (Power: {power})"

    print("\nTesting partial enchanter...")
    enchant = partial_enchanter(base_enchantment)
    print(enchant['fire_enchant']("Sword"))

    print("\nTesting memoized fibonacci...")
    fibonacci = memoized_fibonacci(10)
    print(f"Fib (10): {fibonacci}")

    print("\nTesting spell dispatcher...")
    dispatcher = spell_dispatcher()
    print(dispatcher(42))
    print(dispatcher("Invisibility"))
    print(dispatcher([1, 2, 3]))


if __name__ == "__main__":
    main()
