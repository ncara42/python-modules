"""Module for brewing magical potions using elemental combinations."""

from .elements import create_fire, create_water, create_air, create_earth


def healing_potion() -> str:
    """Brew a healing potion using fire and water elements.
    
    Returns:
        A string describing the brewed healing potion
    """
    return f"Healing potion brewed with {create_fire()} and {create_water()}"


def strength_potion() -> str:
    """Brew a strength potion using earth and fire elements.
    
    Returns:
        A string describing the brewed strength potion
    """
    return f"Strength potion brewed with {create_earth()} and {create_fire()}"


def invisibility_potion() -> str:
    """Brew an invisibility potion using air and water elements.
    
    Returns:
        A string describing the brewed invisibility potion
    """
    template = "Invisibility potion brewed with {} and {}"
    return template.format(create_air(), create_water())


def wisdom_potion() -> str:
    """Brew a wisdom potion using all four elements.
    
    Returns:
        A string describing the brewed wisdom potion
    """
    template = "Wisdom potion brewed with all elements: {} {} {} {}"
    return template.format(create_fire(), create_water(),
                           create_air(), create_earth())
