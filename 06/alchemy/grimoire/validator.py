def validate_ingredients(ingredients: str) -> str:
    list_valid = ["fire", "water", "air", "earth"]
    valid = "VALID" if [i for i in ingredients.split()
                        if i in list_valid] else "INVALID"
    return f"{ingredients} - {valid}"
