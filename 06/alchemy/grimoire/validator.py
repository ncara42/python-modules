"""Module for validating spell ingredients."""


def validate_ingredients(ingredients: str) -> str:
    """Validate spell ingredients against known elemental ingredients.
    
    Args:
        ingredients: Space-separated ingredient names
        
    Returns:
        A string indicating validation status (VALID or INVALID)
    """
    list_valid = ["fire", "water", "air", "earth"]
    valid = "VALID" if [i for i in ingredients.split()
                        if i in list_valid] else "INVALID"
    return f"{ingredients} - {valid}"
