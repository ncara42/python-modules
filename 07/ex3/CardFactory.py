"""
Módulo que define la clase abstracta CardFactory, utilizada como base
para implementar fábricas de cartas en el juego.
"""

from abc import ABC, abstractmethod


class CardFactory(ABC):
    """
    Clase abstracta que define la interfaz para
    crear diferentes tipos de cartas
    y mazos temáticos en el juego.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de CardFactory.
        """
        pass

    @abstractmethod
    def create_creature(self, name_or_power):
        """
        Método abstracto para crear una carta de criatura.

        Args:
            name_or_power: Nombre o nivel de poder de la criatura.
        """
        pass

    @abstractmethod
    def create_spell(self, name_or_power):
        """
        Método abstracto para crear una carta de hechizo.

        Args:
            name_or_power: Nombre o nivel de poder del hechizo.
        """
        pass

    @abstractmethod
    def create_artifact(self, name_or_power):
        """
        Método abstracto para crear una carta de artefacto.

        Args:
            name_or_power: Nombre o nivel de poder del artefacto.
        """
        pass

    @abstractmethod
    def create_themed_deck(self, size: int):
        """
        Método abstracto para crear un mazo temático.

        Args:
            size (int): Tamaño del mazo.
        """
        pass

    @abstractmethod
    def get_supported_types(self):
        """
        Método abstracto para obtener los tipos de cartas soportados.

        Returns:
            dict: Diccionario con los tipos de cartas y sus ejemplos.
        """
        pass
