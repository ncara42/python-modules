"""Module providing custom hierarchical exceptions for garden management."""


class GardenError(Exception):
    """Base class for all exceptions in the garden module."""
    pass


class PlantError(GardenError):
    """Exception raised when plant capacity limits are breached."""
    pass


class WaterError(GardenError):
    """Exception raised when irrigation levels are outside safe parameters."""
    pass


def garden_error(garden: list) -> None:
    """
    Validates the existence of the garden structure.
    """
    if len(garden) == 0:
        raise GardenError("Garden list is uninitialized or empty.")


def plant_error(plants: int) -> None:
    """
    Validates that the plant count does not exceed resource capacity.
    """
    if plants > 10:
        raise PlantError(f"Maximum 10 plants allowed, but found {plants}.")


def water_error(water: int) -> None:
    """
    Checks if water levels are within the operational safety range.
    """
    if water > 5:
        raise WaterError(f"Water level {water} exceeds safety threshold (5).")
    elif water < 0:
        raise WaterError(f"Negative water level ({water}) is "
                         f"physically impossible.")


def main() -> None:
    """
    Execution entry point to demonstrate professional error handling.
    """
    test = [
        lambda: garden_error([]),
        lambda: plant_error(15),
        lambda: water_error(-15)
    ]

    print("=== Custom Garden Errors Demo ===\n")
    print("Testing PlantError...")
    try:
        plant_error(15)
    except PlantError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("Testing WaterError...")
    try:
        water_error(6)
    except WaterError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("Testing catching all garden errors...")

    n = 0
    for _ in test:
        n += 1

    i = 0
    for error in test:
        try:
            error()
        except GardenError as e:
            print(f"Caught a GardenError: {e}")
        i += 1

        if i == n:
            print()

    print("All custom error types work correctly!")


if __name__ == "__main__":
    main()
