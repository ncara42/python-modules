"""
Este módulo define la interfaz `Combatable`, que especifica los métodos
necesarios para implementar habilidades de combate en las cartas.
"""

from abc import ABC, abstractmethod


class Combatable(ABC):
    """
    Interfaz abstracta para habilidades de combate.
    """

    @abstractmethod
    def attack(self, target: str) -> dict:
        """
        Realiza un ataque a un objetivo.

        :param target: Objetivo del ataque.
        :return: Resultado del ataque.
        """
        pass

    @abstractmethod
    def defend(self, incoming_damage: int) -> dict:
        """
        Defiende contra un ataque entrante.

        :param incoming_damage: Daño recibido.
        :return: Resultado de la defensa.
        """
        pass

    @abstractmethod
    def get_combat_stats(self) -> dict:
        """
        Devuelve las estadísticas de combate de la carta.

        :return: Diccionario con las estadísticas de combate.
        """
        pass
