"""Plant manufacturing module."""


class Plant:
    """Represents a basic plant model for manufacturing purposes."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize the plant with manufacturing specifications."""
        self.name = name
        self.height = height
        self.age = age

    def get_info(self) -> None:
        """Print the manufacturing details of the plant instance."""
        print(f"Created: {self.name} ({self.height}cm, {self.age} days)")


def main() -> None:
    """Execute the plant manufacturing process and show summary."""
    garden = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120)
    ]

    for plant in garden:
        
        plant.get_info()

    print()
    print(f"Total plants created: {len(garden)}")


if __name__ == "__main__":
    main()
