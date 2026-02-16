"""Module demonstrating how to avoid circular dependency issues using late imports."""

from alchemy.grimoire.validator import validate_ingredients
from alchemy.grimoire.spellbook import record_spell


def main() -> None:
    """Demonstrate circular dependency resolution with late imports."""
    print("=== Circular Curse Breaking ===")

    print("\nTesting ingredient validation:")
    template = 'validate_ingredients("fire air"): {}'
    print(template.format(validate_ingredients("fire air")))
    template = 'validate_ingredients("dragon scales"): {}'
    print(template.format(validate_ingredients("dragon scales")))

    print("\nTesting spell recording with validation:")
    template = 'record_spell("Fireball", "fire air"): {}'
    print(template.format(record_spell("Fireball", "fire air")))
    template = 'record_spell("Dark Magic", "shadow"): {}'
    print(template.format(record_spell("Dark Magic", "shadow")))

    print("\nTesting late import technique:")
    template = 'record_spell("Lightning", "air"): {}'
    print(template.format(record_spell("Lightning", "air")))

    print("\nCircular dependency curse avoided using late imports!")
    print("All spells are processed safely!")


if __name__ == "__main__":
    main()
