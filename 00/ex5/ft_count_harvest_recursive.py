def ft_count_harvest_recursive(current=1, total=None):
    if total is None:
        total = int(input("Days until harvest: "))
    if current <= total:
        print(f"Day {current}")
        ft_count_harvest_recursive(current + 1, total)
    else:
        print("Harvest time!")
