"""Module for counting down days to harvest iteratively."""


def ft_count_harvest_iterative() -> None:
    """Count down days until harvest using an iterative approach."""
    days = int(input("Days until harvest: "))
    for i in range(1, days + 1):
        print(f"Day {i}")
    print("Harvest time!")
