"""Module to display command-line arguments and metadata."""

import sys


def main() -> None:
    """
    Parse and display command-line arguments provided to the script.

    This function counts total arguments, identifies the program name,
    and enumerates each argument received from the terminal.
    """
    total_args: int = len(sys.argv)

    print("=== Command Quest ===")

    if total_args == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_args - 1}")

        for i, arg in enumerate(sys.argv[1:], start=1):
            print(f"Argument {i}: {arg}")

        print(f"Total arguments: {total_args}")


if __name__ == "__main__":
    main()
