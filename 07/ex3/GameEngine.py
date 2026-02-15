"""
Módulo que define la clase GameEngine, responsable de orquestar el juego
utilizando una fábrica de cartas y una estrategia de juego.
"""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.GameStrategy import GameStrategy


class GameEngine:
    """
    Clase que representa el motor del juego.
    Permite configurar una fábrica de cartas
    y una estrategia de juego, y simular turnos.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de GameEngine.
        """
        self.factory: FantasyCardFactory | None = None
        self.strategy: GameStrategy | None = None
        self.total_turns_simulated: int = 0

    def configure_engine(self, factory, strategy) -> None:
        """
        Configura el motor del juego con una fábrica
        de cartas y una estrategia.

        Args:
            factory (FantasyCardFactory): Fábrica de cartas a utilizar.
            strategy (GameStrategy): Estrategia de juego a utilizar.
        """
        if isinstance(factory, FantasyCardFactory) \
                and isinstance(strategy, GameStrategy):
            self.factory = factory
            self.strategy = strategy
        else:
            print("Factory or strategy is not a valid instance")

    def simulate_turn(self) -> dict:
        """
        Simula un turno del juego utilizando la estrategia configurada.

        Returns:
            dict: Resultado de las acciones realizadas durante el turno.
        """
        print(f"Strategy: {self.strategy.__class__.__name__}")
        if self.factory is None or self.strategy is None:
            print("Engine is not properly configured")
            self.total_turns_simulated += 1
            return {}

        hand = [
            self.factory.create_creature("Dragon"),
            self.factory.create_spell("Fireball"),
            self.factory.create_artifact("Magic Ring")
        ]

        battlefield = [
            {"owner": "player", "card": self.factory.create_creature("Gob")},
            {"owner": "enemy", "card": self.factory.create_creature("Orc")}
        ]

        return self.strategy.execute_turn(hand, battlefield)

    def get_engine_status(self) -> dict:
        """
        Devuelve el estado actual del motor del juego.

        Returns:
            dict: Información sobre el estado del motor,
            incluyendo turnos simulados,
            cartas creadas y estrategia utilizada.
        """
        if self.factory is None:
            raise ValueError("Factory is not configured in the engine.")
        if self.strategy is None:
            raise ValueError("Strategy is not configured in the engine.")

        return {
            "turns_simulated": self.total_turns_simulated,
            "cards_created": self.factory.cards_created,
            "strategy_used": self.strategy.__class__.__name__,
            "total_damage": 100
        }
