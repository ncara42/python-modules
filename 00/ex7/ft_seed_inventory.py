"""Module for managing seed inventory information."""


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    """
    Display seed inventory information.
    
    Args:
        seed_type: Type of seed
        quantity: Amount of seeds
        unit: Unit of measurement (packets, grams, or area)
    """
    name = seed_type.capitalize()
    if unit == "packets":
        print(f"{name} seeds: {quantity} {unit} available")
    elif unit == "grams":
        print(f"{name} seeds: {quantity} {unit} total")
    elif unit == "area":
        print(f"{name} seeds: covers {quantity} {unit} meters")
    else:
        print("Uknown unit type")
