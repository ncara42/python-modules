"""Garden security module."""


class SecurePlant:
    """
    Represents a plant with data integrity.

    This class ensures that sensitive attributes like height and age
    cannot be modified with invalid values.

    Attributes:
        name (str): Name of the plant.
        __height (int): Plant height (protected).
        __age (int): Plant age (protected).
    """

    def __init__(self, name: str, height: int, age: int) -> None:
        """Initialize a secure plant with name, height, and age."""
        self.name = name
        print(f"Plant created: {self.name}")
        self.__height = 0
        self.__age = 0
        self.set_height(height)
        self.set_age(age)

    def set_height(self, value: int) -> None:
        """Validate and set the plant height."""
        if value < 0:
            print(f"\nInvalid operation attmpeted: "
                  f"height {value}cm [REJECTED]")
            print("Security: Negative height rejected")
        else:
            self.__height = value
            print(f"Height updated: {self.get_height()}cm [OK]")

    def set_age(self, value: int) -> None:
        """Validate and set the plant age."""
        if value < 0:
            print(f"\nInvalid operation attempted: age {value} [REJECTED]")
            print("Security: Negative age rejected")
        else:
            self.__age = value
            print(f"Age updated: {self.get_age()} days [OK]")

    def get_age(self) -> int:
        """Return the current age of the plant."""
        return self.__age

    def get_height(self) -> int:
        """Return the current height of the plant."""
        return self.__height


def main() -> None:
    """Organize the execution of the program."""
    print("=== Garden Security System ===")
    rose = SecurePlant("Rose", 20, 30)

    rose.set_height(-15)

    try:
        print(f"{rose.__height}")
    except AttributeError as e:
        print(f"\nError: {e}")

    print(f"\nCurrent plant: {rose.name} "
          f"({rose.get_height()}cm, {rose.get_age()} days)")


if __name__ == "__main__":
    main()
