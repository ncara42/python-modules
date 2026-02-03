"""Module for validating agricultural temperature data streams."""


def check_temperature(temp) -> int | None:
    """
    Validates if a temperature string is a number
    and within safe plant ranges (0-40°C).
    """
    try:
        temp_int = int(temp)
        if 0 <= temp_int <= 40:
            print(f"Temperature {temp_int}°C is perfect for plants!")
            return temp_int
        elif temp_int < 0:
            print(f"Error: {temp_int}°C is too cold for plants (min 0ºC)")
        else:
            print(f"Error: {temp_int}°C is too hot for plants (max 40ºC)")
    except ValueError:
        print(f"Error: '{temp}' is not a valid number")

    return None


def test_temperature_input() -> None:
    """
    Demonstrates the pipeline resilience with
    good, bad, and extreme test values.
    """
    test_values = ["25", "abc", "100", "-50"]

    len = 0
    for _ in test_values:
        len += 1

    i = 0
    for value in test_values:
        print(f"Testing temperature: {value}")
        check_temperature(value)
        i += 1

        if i < len:
            print()


def main() -> None:
    """
    Entry point for the Garden Temperature Checker application.
    """
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("\nAll tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
