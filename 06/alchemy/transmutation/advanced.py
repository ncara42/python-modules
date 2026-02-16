"""Module for advanced transmutation operations."""

from .basic import lead_to_gold
from ..potions import healing_potion


def philosopers_stone() -> str:
    """Create the philosopher's stone using gold and healing potion.
    
    Returns:
        A string describing the philosopher's stone creation
    """
    template = "Philosopher's stone created using {} and {}"
    return template.format(lead_to_gold(), healing_potion())


def elixir_of_life() -> str:
    """Create the elixir of life for eternal youth.
    
    Returns:
        A string describing the elixir of life
    """
    return "Elixir of life: eternal youth achieved!"
