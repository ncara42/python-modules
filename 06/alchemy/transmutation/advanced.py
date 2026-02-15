from .basic import lead_to_gold
from ..potions import healing_potion


def philosopers_stone() -> str:
    template = "Philosopher's stone created using {} and {}"
    return template.format(lead_to_gold(), healing_potion())


def elixir_of_life() -> str:
    return "Elixir of life: eternal youth achieved!"
