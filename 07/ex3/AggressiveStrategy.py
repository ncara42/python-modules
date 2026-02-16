"""
Módulo que define la clase AggressiveStrategy, una estrategia de juego
que prioriza el ataque agresivo en cada turno.
"""

from ex3.GameStrategy import GameStrategy


class AggressiveStrategy(GameStrategy):
    """
    Clase que implementa una estrategia agresiva para el juego.
    Esta estrategia prioriza atacar con todas las cartas disponibles
    y seleccionar objetivos con menor salud.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de AggressiveStrategy.
        """
        super().__init__()

    def execute_turn(self, hand: list, battlefield: list) -> dict:
        """
        Ejecuta un turno agresivo utilizando las cartas en mano y atacando
        a los objetivos en el campo de batalla.

        Args:
            hand (list): Lista de cartas en la mano del jugador.
            battlefield (list): Lista de objetivos en el campo de batalla.

        Returns:
            dict: Acciones realizadas durante el turno,
            incluyendo cartas jugadas, objetivos atacados y daño infligido.
        """
        actions = {
            "cards_played": [
                f"{card.name} ({card.attack})" for card in hand
                if hasattr(card, "attack")
            ],
            "targets_attacked": [
                f"{target['card'].name}" for target in battlefield
            ],
            "damage_dealt": sum(
                card.attack for card in hand if hasattr(card, "attack")
            )
        }
        return actions

    def get_strategy_name(self) -> str:
        """
        Devuelve el nombre de la estrategia.

        Returns:
            str: Nombre de la estrategia.
        """
        return "AgressiveStrategy"

    def prioritize_targets(self, available_targets: list) -> list:
        """
        Prioriza los objetivos disponibles en función de su salud.

        Args:
            available_targets (list): Lista de objetivos disponibles.

        Returns:
            list: Lista de objetivos ordenados por prioridad.
        """
        def get_priority(target: dict) -> float:
            """
            Returns the priority value for a target based on health.

            Args:
                target (dict): Target to evaluate.

            Returns:
                float: Priority value.
            """
            return target.get('health', float('inf'))

        return sorted(available_targets, key=get_priority)
