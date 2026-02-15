def record_spell(spell_name: str, ingredients: str) -> str:
    from .validator import validate_ingredients

    valid = validate_ingredients(ingredients)
    status = "recorded" if "VALID" in valid else "rejected"
    return f"Spell {status}: {spell_name} ({valid})"
