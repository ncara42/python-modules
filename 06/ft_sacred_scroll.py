import alchemy


def main():
    print("=== Sacred Scroll Mastery ===")

    print("\nTesting direct module access:")
    print(f"alchemy.element.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.element.create_water(): {alchemy.elements.create_water()}")
    print(f"alchemy.element.create_earth(): {alchemy.elements.create_earth()}")
    print(f"alchemy.element.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        print(f"alchemy.create_fire(): {alchemy.create_fire()}")
    except AttributeError as e:
        print(f"{alchemy.create_fire} {type(e).__name__} - not exposed")

    try:
        print(f"alchemy.create_water(): {alchemy.create_water()}")
    except AttributeError as e:
        print(f"{alchemy.create_water} {type(e).__name__} - not exposed")

    try:
        print(f"alchemy.create_earth(): {alchemy.create_earth()}")
    except AttributeError as e:
        print(f"alchemy.create_earth(): {type(e).__name__} - not exposed")

    try:
        print(f"alchemy.create_air(): {alchemy.create_air()}")
    except AttributeError as e:
        print(f"alchemy.create_air(): {type(e).__name__} - not exposed")

    print("\nPackage metadata:")
    print(f"Version: {alchemy.__version__}")
    print(f"Author: {alchemy.__author__}")


if __name__ == "__main__":
    main()
