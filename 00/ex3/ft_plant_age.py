"""Module for checking if a plant is ready for harvest."""


def ft_plant_age() -> None:
    """Check plant age and determine if it's ready to harvest (>60 days)."""
    age = int(input("Enter plant age in days: "))
    if (age > 60):
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
