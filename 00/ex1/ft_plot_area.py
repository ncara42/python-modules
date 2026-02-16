"""Module for calculating garden plot area."""


def ft_plot_area() -> None:
    """Calculate and display the area of a garden plot based on user input."""
    length = int(input("Enter length: "))
    width = int(input("Enter width: "))
    area = length * width
    print(f"Plot area: {area}")
