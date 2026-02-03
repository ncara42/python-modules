"""Garden management module."""


class Plant:
    """Stores specific information about a plant instance."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


def main() -> None:
    """Organize the execution of the garden registry simulation."""
    garden = [
        Plant("Rose", 25, 30),
        Plant("Sunflower", 80, 45),
        Plant("Cactus", 15, 120)
    ]

    print("=== Garden Plant Registry ===")
    for plant in garden:
        print(f"{plant.name}: {plant.height}cm, {plant.age} days old")


if __name__ == "__main__":
    main()
