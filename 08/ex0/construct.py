"""
This script provides utilities to check the current Python
environment and manage virtual environments.
It helps users identify whether they are in a virtual
environment and provides instructions for setting one up.
"""

import sys
import site


def is_virtual_env() -> bool:
    """
    Determines if the current Python interpreter is
    running in a virtual environment.

    Returns:
        bool: True if in a virtual environment, False otherwise.
    """
    return sys.base_prefix != sys.prefix


def show_environment_info() -> None:
    """
    Displays information about the current Python environment.

    If in a virtual environment, it shows the environment name and path.
    Otherwise, it indicates that no virtual environment is detected.
    """
    if is_virtual_env():
        env_name = sys.prefix.split('/')[-1]
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {env_name}")
        print(f"Environment Path: {sys.prefix}")
    else:
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")


def show_virtual_env_instructions() -> None:
    """
    Prints instructions for creating and activating a virtual environment.

    The instructions are tailored for both Unix and Windows systems.
    """
    print("WARNING: You're in the global environment")
    print("The machine can see everything you install\n")
    print("To enter the construct, run:")
    print("python3 -m venv matrix_env")
    print("source matrix_env/bin/activate  # On Unix")
    print("matrix_env\\Scripts\\activate  # On Windows")


def main() -> None:
    """
    Main function to check the Python environment and provide
    relevant information or instructions.

    If in a virtual environment, it displays environment details
    and package installation path.
    Otherwise, it provides instructions to set up and
    activate a virtual environment.
    """
    if is_virtual_env():
        print("MATRIX STATUS: Welcome to the construct")
        print()
        show_environment_info()
        print()
        print("SUCCESS: You're in an isolated environment!")
        print("Safe to install packages without affecting the global system.")
        print()
        print("Package installation path:")
        print(site.getsitepackages()[0])

    else:
        print("MATRIX STATUS: You're still plugged in")
        print()
        show_environment_info()
        print()
        show_virtual_env_instructions()
        print()
        print("Then run this program again")


if __name__ == "__main__":
    main()
