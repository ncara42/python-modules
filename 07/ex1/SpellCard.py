"""Module defining the SpellCard class and EffectType enum for spell cards in DataDeck."""

from ex0.Card import Card
from enum import Enum


class EffectType(Enum):
    """Enumeration of possible spell effect types."""
    DAMAGE = "damage"
    HEAL = "heal"
    BUFF = "buff"
    DEBUFF = "debuff"


class SpellCard(Card):
    """
    Clase concreta que representa una carta de hechizo en el sistema DataDeck.
    Los hechizos tienen efectos instantáneos y se consumen al ser jugados.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, effect_type: str) -> None:
        """
        Inicializa una carta de hechizo con un tipo de efecto específico.

        :param name: Nombre de la carta.
        :param cost: Costo de maná para jugar la carta.
        :param rarity: Rareza de la carta.
        :param effect_type: Tipo de efecto del hechizo (daño, curación, etc.).
        """
        super().__init__(name, cost, rarity)
        self.effect_type: str = effect_type

    def play(self, game_state: dict) -> dict:
        """
        Juega la carta de hechizo, aplicando su efecto al estado del juego.

        :param game_state: Estado actual del juego.
        :return: Resultado de jugar la carta.
        """
        if game_state["mana"] < self.cost:
            return {
                'card_played': None,
                'mana_used': 0,
                'effect': "Not enough mana"
            }

        game_state["mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.resolve_effect(["Dragon", "Goblin"])["description"]
        }

    def resolve_effect(self, targets: list) -> dict:
        """
        Resuelve el efecto del hechizo en los objetivos especificados.

        :param targets: Lista de objetivos del hechizo.
        :return: Descripción del efecto aplicado.
        """
        if self.effect_type == EffectType.DAMAGE.value:
            return {
                "effect": "Deal damage to target",
                "targets": targets,
                "description": f"{self.name} deals 3 damage to target"
            }
        elif self.effect_type == EffectType.HEAL.value:
            return {
                "effect": "Heal target",
                "targets": targets,
                "description": f"{self.name} restores 5 health to target"
            }
        elif self.effect_type == EffectType.BUFF.value:
            return {
                "effect": "Buff target",
                "targets": targets,
                "description": f"{self.name} increases the stats of target"
            }
        elif self.effect_type == EffectType.DEBUFF.value:
            return {
                "effect": "Debuff target",
                "targets": targets,
                "description": f"{self.name} decreases the stats of target"
            }
        else:
            return {
                "effect": "Unknown",
                "targets": targets,
                "description": "Effect type not recognized"
            }
