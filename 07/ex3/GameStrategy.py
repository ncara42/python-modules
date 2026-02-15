"""
Módulo que define la clase abstracta GameStrategy, utilizada como base
para implementar diferentes estrategias de juego.
"""

from abc import ABC, abstractmethod


class GameStrategy(ABC):
    """
    Clase abstracta que define la interfaz para
    implementar estrategias de juego.
    Las estrategias determinan cómo se ejecutan
    los turnos y se priorizan los objetivos.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de GameStrategy.
        """
        pass

    @abstractmethod
    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Método abstracto para ejecutar un turno de juego.

        Args:
            hand (list): Lista de cartas en la mano del jugador.
            battlefield (list): Lista de objetivos en el campo de batalla.

        Returns:
            dict: Acciones realizadas durante el turno.
        """
        pass

    @abstractmethod
    def get_strategy_name(self) -> str:
        """
        Método abstracto para obtener el nombre de la estrategia.

        Returns:
            str: Nombre de la estrategia.
        """
        pass

    @abstractmethod
    def prioritize_targets(self, available_targets: list) -> list:
        """
        Método abstracto para priorizar los objetivos disponibles.

        Args:
            available_targets (list): Lista de objetivos disponibles.

        Returns:
            list: Lista de objetivos ordenados por prioridad.
        """
        pass
