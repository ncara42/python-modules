"""
Módulo principal que inicializa y ejecuta el motor del juego utilizando
una fábrica de cartas y una estrategia agresiva.
"""

from ex3.FantasyCardFactory import FantasyCardFactory
from ex3.AggressiveStrategy import AggressiveStrategy
from ex3.GameEngine import GameEngine


def main() -> None:
    """
    Función principal que configura y ejecuta el motor del juego.
    Simula un turno utilizando la estrategia
    agresiva y muestra un informe
    del estado del juego.
    """
    print("=== DataDeck Game Engine ===")
    print()

    engine = GameEngine()
    factory = FantasyCardFactory()
    strategy = AggressiveStrategy()

    print("Configuring Fantasy Card Game....")
    engine.configure_engine(factory, strategy)

    print("Factory: FantasyCardFactory")
    print("Strategy: AgressiveStrategy")
    print(f"Available types: {factory.get_supported_types()}")

    print("\nSimulating aggressive turn...")

    hand = [
        card for card in [
            factory.create_creature("Fire Dragon"),
            factory.create_creature("Goblin Warrior"),
            None,
            factory.create_spell("Fireball")
        ] if card is not None
    ]

    print(
        "Hand:", [
            f"{card.name} "
            f"({card.attack if hasattr(card, 'attack') else 'N/A'})"
            for card in hand
        ]
    )
    print()

    print("Turn execution:")
    turn_execution = engine.simulate_turn()
    print(turn_execution)
    print()

    print("Game report:")
    print(engine.get_engine_status())
    print()

    print("Abstract Factory + Strategy Pattern: Maximum flexibility achieved!")


if __name__ == "__main__":
    main()
