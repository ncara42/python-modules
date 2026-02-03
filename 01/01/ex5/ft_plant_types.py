"""Module for specialized plant types and garden management."""


class Plant:
    """Base class representing the fundamental attributes of any plant."""

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize basic plant data including name, height, and age."""
        self.name = name
        self.height = height
        self.age = age


class Flower(Plant):
    """Class representing flowering plants with aesthetic features."""

    def __init__(self, name: str, height: int, age: int, color: str) -> None:
        """Initialize a flower with an additional color attribute."""
        super().__init__(name, height, age)
        self.color = color

    def bloom(self) -> None:
        """Display a blooming message for the flower."""
        self.show_info()

    def show_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.color} color")
        print(f"{self.name} is blooming beautifully!")


class Tree(Plant):
    """Class representing trees with structural measurements."""

    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """Initialize a tree with its specific trunk diameter."""
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter

    def produce_shade(self) -> None:
        """Display the shade coverage based on the trunk diameter."""
        self.show_info()

    def show_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.trunk_diameter}cm diameter")
        print(f"{self.name} provides {self.trunk_diameter} "
              f"square meters of shade")

class Vegetable(Plant):
    """Class representing edible plants with nutritional and seasonal data."""

    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """Initialize a vegetable with harvest timing and vitamin content."""
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value

    def show_nutrition(self) -> None:
        """Display the specific vitamin content of the vegetable."""
        self.show_info()

    def show_info(self):
        print(f"{self.name} ({self.__class__.__name__}): {self.harvest_season}")
        print(f"{self.name} is rich in vitamin {self.nutritional_value}")

def main() -> None:
    """Execute the garden demonstration and display plant specialized info."""
    garden = [
        Flower("Rose", 25, 30, "red"),
        Flower("Sunflower", 55, 10, "yellow"),
        Tree("Oak", 500, 1825, 50),
        Tree("Pine", 300, 1103, 30),
        Vegetable("Tomato", 80, 90, "summer harvest", "C"),
        Vegetable("Carrot", 20, 70, "autumn harvest", "A")
    ]

    print("=== Garden Plant Types ===\n")

    len = 0
    for plant in garden:
        len += 1

    i = 0
    for  plant in garden:
        info = (f"{plant.name} ({type(plant).__name__}): "
                f"{plant.height}cm, {plant.age} days")

        plant.show_info()
        i += 1

        if i < len:
            print()
           

if __name__ == "__main__":
    main()
