"""Module to demonstrate handling of different Python exceptions."""


def garden_operations(error_type: str) -> None:
    """
    Triggers specific exceptions based on the provided error_type.
    """
    if error_type == "ValueError":
        int("abc")
    elif error_type == "ZeroDivisionError":
        10 / 0
    elif error_type == "FileNotFoundError":
        open("missing.txt", "r")
    elif error_type == "KeyError":
        {}["missing_plant"]


def test_error_types() -> None:
    """
    Tests and catches individual garden exceptions using try-except blocks.
    """
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("ValueError")
    except ValueError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        garden_operations("ZeroDivisionError")
    except ZeroDivisionError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        garden_operations("FileNotFoundError")
    except FileNotFoundError as e:
        print(f"Caught {type(e).__name__}: {e}\n")

    print("Testing KeyError...")
    try:
        garden_operations("KeyError")
    except KeyError as e:
        print(f"Caught {type(e).__name__}: {e}\n")


def main() -> None:
    """
    Main entry point to run individual and multiple error tests.
    """
    test_error_types()
    print("Testing multiple errors together...")

    try:
        garden_operations("ValueError")
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")

    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
