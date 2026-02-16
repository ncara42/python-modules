"""Module for counting down days to harvest recursively."""


def ft_count_harvest_recursive(current: int = 1, total: int = None) -> None:
    """
    Count down days until harvest using a recursive approach.
    
    Args:
        current: Current day number (starts at 1)
        total: Total number of days until harvest
    """
    if total is None:
        total = int(input("Days until harvest: "))
    if current <= total:
        print(f"Day {current}")
        ft_count_harvest_recursive(current + 1, total)
    else:
        print("Harvest time!")
