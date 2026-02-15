"""
Garden Guardian: A robust plant management system.
This module handles plant data validation and resilient error recovery.
"""


class GardenError(Exception):
    """Base exception for all garden-related issues."""
    pass


class PlantValidationError(GardenError):
    """Exception raised for errors in the plant naming or data."""
    pass


class HealthError(GardenError):
    """Exception raised for plants out of healthy water/sun ranges."""
    pass


class Plant:
    """Represents a plant with its growth requirements."""
    def __init__(self, name, water_level: int, sun_hours: int) -> None:
        self.name = name
        self.water_level = water_level
        self.sun_hours = sun_hours


class GardenManager:
    """Manages a collection of plants with fault-tolerant operations."""
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []

    def add_plants(self, plant: Plant) -> None:
        """Adds a plant using list concatenation and validates name."""
        if not plant.name:
            raise PlantValidationError("Plant name cannot be empty!")
        self.plants = self.plants + [plant]

    def water_all(self) -> None:
        """Simulates irrigation with mandatory resource cleanup."""
        print("Opening watering system")
        try:
            for plant in self.plants:
                print(f"Watering {plant.name} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self) -> None:
        """Iterates through plants and validates vital levels individually."""
        for plant in self.plants:
            try:
                if 1 <= plant.water_level <= 10 and 2 <= plant.sun_hours <= 12:
                    print(f"{plant.name}: healthy (water: {plant.water_level},"
                          f" sun: {plant.sun_hours})")
                elif plant.water_level > 10:
                    raise HealthError(f"Water level {plant.water_level} "
                                      f"is too high (max 10)")
                elif plant.water_level < 1:
                    raise HealthError(f"Water level {plant.water_level} "
                                      f"is too low (min 1)")
                elif plant.sun_hours > 12:
                    raise HealthError(f"Sunlight hours {plant.sun_hours} "
                                      f"is too high (max 12)")
                elif plant.sun_hours < 2:
                    raise HealthError(f"Sunlight hours {plant.sun_hours} "
                                      f"is too low (min 2)")
            except HealthError as e:
                print(f"Error checking {plant.name}: {e}")


def main() -> None:
    """Main execution flow demonstrating error recovery and resilience."""
    noel = GardenManager("Noel")

    # Input with intentionally bad data
    garden_input = [
        Plant("Tomato", 7, 3),
        Plant("Lettuce", 15, 6),
        Plant(None, 10, 12)
    ]

    print("=== Garden Management System ===\n")

    print("Adding plants to garden...")
    for p in garden_input:
        try:
            noel.add_plants(p)
            print(f"Added {p.name} successfully")
        except PlantValidationError as e:
            print(f"Error adding plant: {e}")

    print("\nWatering plants...")
    noel.water_all()

    print("\nChecking plant health...")
    noel.check_health()

    print("\nTesting error recovery...")
    try:
        raise GardenError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("\nGarden management system test complete!")


if __name__ == "__main__":
    main()
