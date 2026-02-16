"""Module for calculating total harvest over three days."""


def ft_harvest_total() -> None:
    """Calculate and display the total harvest from three days of collection."""
    day1 = int(input("Day 1 harvest: "))
    day2 = int(input("Day 2 harvest: "))
    day3 = int(input("Day 3 harvest: "))
    total = day1 + day2 + day3
    print(f"Total harvest: {total}")
