"""Docstrings"""


import sys

def main():
    total_args = len(sys.argv)

    print("=== Command Quest ===")

    if len(sys.argv) == 1:
        print("No arguments provided!")
        print(f"Program name: {sys.argv[0]}")
        print(f"Total arguments: {total_args}")
    else:
        print(f"Program name: {sys.argv[0]}")
        print(f"Arguments received: {total_args}")
        for i, args in enumerate(sys.argv[1:], start=1):
                print(f"Argument {i}: {sys.argv[i]}")
        print(f"Total arguments: {total_args}")

if __name__ == "__main__":
    main()
