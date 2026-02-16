"""Module for recording spells in the grimoire."""


def record_spell(spell_name: str, ingredients: str) -> str:
    """Record a spell with validated ingredients.
    
    Args:
        spell_name: Name of the spell to record
        ingredients: Space-separated ingredient names
        
    Returns:
        A string indicating whether the spell was recorded or rejected
    """
    from .validator import validate_ingredients

    valid = validate_ingredients(ingredients)
    status = "recorded" if "VALID" in valid else "rejected"
    return f"Spell {status}: {spell_name} ({valid})"
