"""Plant growth simulation module."""


class Plant:
    """Stores and manages the growth data of a specific plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with its name, height, and age."""
        self.name = name
        self.height = height
        self.age = age

    def age_plant(self) -> None:
        """Increment the plant's age by one day."""
        self.age += 1

    def grow_plant(self) -> None:
        """Increase the plant's height by one centimeter."""
        self.height += 1

    def get_info(self) -> None:
        """Display the current status of the plant."""
        print(f"{self.name}: {self.height}cm, {self.age} days old")


def main() -> None:
    """Simulate a week of growth for a specific plant."""
    rose = Plant("Rose", 25, 30)

    print("=== Day 1 ===")
    rose.get_info()

    last_grow = 6
    for _ in range(last_grow):
        rose.age_plant()
        rose.grow_plant()

    print("=== Day 7 ===")
    rose.get_info()

    print(f"Growth this week: +{last_grow}cm")


if __name__ == "__main__":
    main()
