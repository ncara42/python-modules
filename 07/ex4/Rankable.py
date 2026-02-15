"""
Módulo que define la interfaz Rankable, utilizada para implementar
funcionalidades relacionadas con el ranking de cartas en torneos.
"""

from abc import ABC, abstractmethod


class Rankable(ABC):
    """
    Interfaz abstracta que define los métodos necesarios para calcular
    el ranking, actualizar victorias y derrotas, y obtener información
    del ranking de una carta.
    """

    @abstractmethod
    def calculate_rating(self) -> int:
        """
        Calcula el puntaje de la carta basado en su desempeño.

        Returns:
            int: Puntaje calculado.
        """
        pass

    @abstractmethod
    def update_wins(self, wins: int) -> None:
        """
        Actualiza el número de victorias de la carta.

        Args:
            wins (int): Número de victorias a añadir.
        """
        pass

    @abstractmethod
    def update_losses(self, losses: int) -> None:
        """
        Actualiza el número de derrotas de la carta.

        Args:
            losses (int): Número de derrotas a añadir.
        """
        pass

    @abstractmethod
    def get_rank_info(self) -> dict:
        """
        Devuelve información detallada sobre el ranking de la carta.

        Returns:
            dict: Información del ranking.
        """
        pass
