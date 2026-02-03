"""Module for managing different types of plants and garden statistics."""


class Plant:
    """Base class representing a generic plant."""

    def __init__(self, name: str, height: int) -> None:
        """Initialize a plant with a name and height."""
        self.name = name
        self.height = height

    d
class FloweringPlant(Plant):
    """Class representing a plant that produces flowers."""

    def __init__(self, name: str, height: int, color: str) -> None:
        """Initialize a flowering plant with an additional flower color."""
        super().__init__(name, height)
        self.color = color


class PrizeFlower(FloweringPlant):
    """Class representing a competition-grade flowering plant with points."""

    def __init__(self, name: str, height: int,
                 color: str, points: int) -> None:
        """Initialize a prize flower with competition points."""
        super().__init__(name, height, color)
        self.points = points


class GardenManager:
    """Manager class to handle garden operations and global statistics."""

    total_gardens = 0
    grow_count = 0

    def __init__(self, owner: str) -> None:
        """Initialize the garden manager for a specific owner."""
        self.owner = owner
        self.plants = []
        GardenManager.total_gardens += 1

    def add_plant(self, plant: Plant) -> None:
        """Add a plant object to the garden list."""
        self.plants += [plant]

    def grow(self) -> None:
        """Increase the height of all plants in the garden by 1cm."""
        print(f"\n{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.height += 1
            print(f"{plant.name} grew 1cm")
            GardenManager.grow_count += 1

    class GardenStats:
        """Inner class for calculating garden composition reports."""

        @staticmethod
        def get_report(plants: list) -> dict:
            """
            Count the occurrence of each plant
            type and return a dictionary.
            """
            counts = {"regular": 0, "flowering": 0, "prize": 0}
            for i in plants:
                if isinstance(i, PrizeFlower):
                    counts["prize"] += 1
                elif isinstance(i, FloweringPlant):
                    counts["flowering"] += 1
                else:
                    counts["regular"] += 1
            return counts

    def show_report(self) -> None:
        """Display a full report of the garden status."""
        report = self.GardenStats.get_report(self.plants)

        print("=== Garden Management System Demo ===\n")
        for plant in self.plants:
            print(f"Added {plant.name} to {self.owner}'s garden")

        self.grow()

        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")

        for plant in self.plants:
            if isinstance(plant, PrizeFlower):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming), "
                      f"prize points: {plant.points}")
            elif isinstance(plant, FloweringPlant):
                print(f"- {plant.name}: {plant.height}cm, "
                      f"{plant.color} flowers (blooming)")
            elif isinstance(plant, Plant):
                print(f"- {plant.name}: {plant.height}cm")

        print(f"\nPlants added: {len(self.plants)}. "
              f"Total growth: {GardenManager.grow_count}cm")
        print(f"Plant types: {report['regular']} regular, "
              f"{report['flowering']} flowering, "
              f"{report['prize']} prize flowers")

    @classmethod
    def create_garden_network(cls) -> None:
        """Display global statistics for all managed gardens."""
        print(f"Total gardens managed: {cls.total_gardens}")

    @staticmethod
    def validate_height(h: int) -> bool:
        """Check if a given height is a valid positive number."""
        return h > 0


def main() -> None:
    """Main execution function for the garden demo."""
    alice = GardenManager("Alice")
    bob = GardenManager("Bob")

    garden_a = [
        Plant("Oak Tree", 100),
        FloweringPlant("Rose", 25, "red"),
        PrizeFlower("Sunflower", 50, "yellow", 10)
    ]

    garden_b = [
        Plant("Oak", 70),
        FloweringPlant("Cactus", 25, "green")
    ]

    for plant in garden_a:
        alice.add_plant(plant)

    alice.show_report()

    alice_score = 0
    for plant in alice.plants:
        alice_score += plant.height

    for plant in garden_b:
        bob.add_plant(plant)

    bob_score = 0
    for plant in bob.plants:
        bob_score += plant.height

    print(f"\nHeight validation test: {GardenManager.validate_height(101)}")
    print(f"Garden scores - {alice.owner}: {alice_score}, "
          f"{bob.owner}: {bob_score}")
    GardenManager.create_garden_network()


if __name__ == "__main__":
    main()
