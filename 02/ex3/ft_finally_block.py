"""Module demonstrating the use of finally blocks for resource cleanup."""


class PlantError(Exception):
    """Exception raised when a plant is invalid for watering."""
    pass


def water_plants(plant_list: list) -> None:
    """
    Waters a list of plants and ensures the system closes using finally.
    """
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant is None:
                raise PlantError(f"Cannot water {plant} - invalid plant!")
            print(f"Watering {plant}")
    except PlantError as e:
        print(f"Error: {e}")
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system() -> None:
    """
    Runs test cases for normal and erroneous watering operations.
    """
    print("=== Garden Watering System ===\n")

    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("Watering completed successfully!\n")

    print("Testing with error...")
    water_plants(["tomato", None])
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
