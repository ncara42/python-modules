"""Module for displaying garden summary information."""


def ft_garden_summary() -> None:
    """Display a summary of garden information including name and plant count."""
    garden = str(input("Enter garden name: "))
    plants = int(input("Enter number of plants: "))
    print(f"Garden: {garden}")
    print(f"Plants: {plants}")
    print("Status: Growing well!")
