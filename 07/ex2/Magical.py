"""
Este módulo define la interfaz `Magical`, que especifica los métodos
necesarios para implementar habilidades mágicas en las cartas.
"""

from abc import ABC, abstractmethod


class Magical(ABC):
    """
    Interfaz abstracta para habilidades mágicas.
    """

    @abstractmethod
    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Lanza un hechizo a los objetivos especificados.

        :param spell_name: Nombre del hechizo.
        :param targets: Lista de objetivos del hechizo.
        :return: Resultado del hechizo.
        """
        pass

    @abstractmethod
    def channel_mana(self, amount: int) -> dict:
        """
        Canaliza una cantidad específica de maná.

        :param amount: Cantidad de maná a canalizar.
        :return: Resultado de la canalización.
        """
        pass

    @abstractmethod
    def get_magic_stats(self) -> dict:
        """
        Devuelve las estadísticas mágicas de la carta.

        :return: Diccionario con las estadísticas mágicas.
        """
        pass
