"""Module for checking if plants need watering."""


def ft_water_reminder() -> None:
    """Check days since last watering and remind to water if needed."""
    days = int(input("Days since last watering: "))
    if (days > 2):
        print("Water the plants!")
    else:
        print("Plants are fine")
