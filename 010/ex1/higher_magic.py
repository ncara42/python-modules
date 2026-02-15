from typing import Callable, Any


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    return lambda *args: (spell1(*args), spell2(*args))


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    return lambda *args: (base_spell(*args)) * multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    return lambda *args: spell(*args) if condition(*args) else "Spell fizzled"


def spell_sequence(spells: list[spell]) -> Callable[..., list[int]]:
    return lambda *args: [spell(*args) for spell in spells]


# I must play with those defs for proving how it works!
def spell1(num: int, count: int = 0) -> int:
    return num + count


def spell2(num: int, count: int = 1) -> int:
    return num * count


def cast_spell(num: int) -> bool:
    return num > 50


def main():
    print("Testing spell combiner...")
    combined: Callable[..., tuple[int, int]] = spell_combiner(spell1, spell2)
    print(combined(0, 8))

    print("\nTesting power amplifier...")
    amplified: Callable[..., tuple[int, int]] = power_amplifier(spell2, 10)
    print(amplified(5, 1))

    print("\nTesting conditional caster...")
    casted: Callable[..., tuple[int, int]]  = conditional_caster(cast_spell, spell2)
    print(casted(55))

    print("\nTesting spell sequence...")
    spelled: Callable[..., tuple[int, int]] = spell_sequence([spell1, spell2])
    print(spelled(50, 1))


if __name__ == "__main__":
    main()
