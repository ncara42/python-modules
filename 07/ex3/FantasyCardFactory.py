"""
Módulo que define la clase FantasyCardFactory,
responsable de crear cartas temáticas
para un juego de fantasía. Implementa métodos para
generar criaturas, hechizos y
artefactos, así como mazos temáticos.
"""

from ex3.CardFactory import CardFactory
from random import randint
from ex1.ArtifactCard import ArtifactCard
from ex1.SpellCard import SpellCard, EffectType
from ex0.CreatureCard import CreatureCard
from ex0.main import Rarity
from typing import Optional


class FantasyCardFactory(CardFactory):
    """
    Clase que extiende CardFactory para crear cartas
    específicas de fantasía.
    Proporciona métodos para generar criaturas,
    hechizos, artefactos y mazos temáticos.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de FantasyCardFactory.
        """
        super().__init__()
        self.cards_created: int = 0

    def create_creature(self, name_or_power: str | int) -> CreatureCard | None:
        """
        Crea una carta de criatura basada en un nombre o un nivel de poder.

        Args:
            name_or_power (str | int): Nombre de la criatura o nivel de poder.

        Returns:
            CreatureCard | None: Una carta de criatura o
            None si el argumento no es válido.
        """
        if isinstance(name_or_power, int):
            self.cards_created += 1
            return CreatureCard(
                "Generic Creature", 5,
                Rarity.RARE.value, name_or_power, 100
            )
        if isinstance(name_or_power, str):
            power = randint(1, 5)
            self.cards_created += 1
            return CreatureCard(
                name_or_power, 5,
                Rarity.RARE.value, power, 100
            )
        else:
            return None

    def create_spell(self, name_or_power: str | int) -> SpellCard | None:
        """
        Crea una carta de hechizo basada en un nombre o un nivel de poder.

        Args:
            name_or_power (str): Nombre del hechizo.

        Returns:
            SpellCard: Una carta de hechizo.
        """
        if isinstance(name_or_power, str):
            power = randint(1, 5)
            self.cards_created += 1
            return SpellCard(
                name_or_power, power,
                Rarity.RARE.value, EffectType.DAMAGE.value
            )

    def create_artifact(self, name_or_power: str | int) -> Optional[ArtifactCard]:
        """
        Crea una carta de artefacto basada en un nombre.

        Args:
            name_or_power (str): Nombre del artefacto.

        Returns:
            Optional[ArtifactCard]: Una carta de artefacto
            o None si el argumento no es válido.
        """
        if isinstance(name_or_power, str):
            self.cards_created += 1
            return ArtifactCard(
                name_or_power, 5,
                Rarity.RARE.value, 15, EffectType.DAMAGE.value
            )

    def create_themed_deck(self, size: int) -> dict:
        """
        Crea un mazo temático con criaturas, hechizos y artefactos.

        Args:
            size (int): Tamaño del mazo.

        Returns:
            dict: Un diccionario que contiene listas
            de cartas clasificadas por tipo.
        """
        deck = {
            "creatures": [
                self.create_creature("Dragon") for _ in range(size // 3)
            ],
            "spells": [
                self.create_spell("Fireball") for _ in range(size // 3)
            ],
            "artifacts": [
                self.create_artifact("Magic Ring") for _ in range(size // 3)
            ],
        }
        return deck

    def get_supported_types(self) -> dict:
        """
        Devuelve los tipos de cartas soportados por la fábrica.

        Returns:
            dict: Un diccionario con los tipos de cartas y sus ejemplos.
        """
        return {
            "creatures": ["Dragon", "Goblin", "Lightning Bolt"],
            "spells": ["Fireball"],
            "artifacts": ["mana_ring"]
        }
