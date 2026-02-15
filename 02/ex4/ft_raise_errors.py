"""Module for validating plant health parameters using raise statements."""


def check_plant_health(plant_name, water_level: int,
                       sunlight_hours: int) -> None:
    """
    Validates plant data and raises ValueError if parameters are out of range.
    """
    if not plant_name:
        raise ValueError("Plant name cannot be empty!")

    if water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")

    if sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too high (max 12)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         f"is too low (min 2)")


def test_plan_checks() -> None:
    """
    Tests the check_plant_health function with various valid and invalid inputs
    """
    print("=== Garden Plant Health Checker ===\n")

    print("Testing good values...")
    try:
        check_plant_health("Tomato", 10, 5)
        print("Plant 'Tomato' is healthy!")
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 15, 60)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad water level...")
    try:
        check_plant_health("Tomato", 15, 12)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("Tomato", 5, 1)
    except ValueError as e:
        print(f"Error: {e}")

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plan_checks()
