"""
Módulo principal que inicializa y ejecuta la plataforma de torneos.
Registra cartas, simula partidas y genera reportes del torneo.
"""

from ex4.TournamentPlatform import TournamentPlatform
from ex4.TournamentCard import TournamentCard


def main() -> None:
    """
    Función principal que configura y ejecuta la plataforma de torneos.
    Registra cartas, simula una partida y muestra el estado del torneo.
    """
    print("=== DataDeck Torunament Platform ===")

    print("\nRegistering Tournament Cards...")

    fire_dragon = TournamentCard(
        name="Fire Dragon",
        cost=5,
        rarity="Epic",
        damage=50,
        defense=30,
        health=100,
        combat_type="Fire"
    )

    ice_wizard = TournamentCard(
        name="Ice Wizard",
        cost=4,
        rarity="Rare",
        damage=40,
        defense=20,
        health=80,
        combat_type="Ice"
    )

    platform = TournamentPlatform()

    fire_dragon_id = platform.register_card(fire_dragon)
    ice_wizard_id = platform.register_card(ice_wizard)

    platform.print_card_info(fire_dragon_id)
    print()
    platform.print_card_info(ice_wizard_id)

    print("\nCreating tournament match...")
    match_result = platform.create_match(fire_dragon_id, ice_wizard_id)
    print(f"Match result: {match_result}")
    print()
    platform.get_leaderboard()
    print()

    print("Platform Report:")
    print(platform.generate_tournament_report())
    print()

    print("=== Tournament Platform Successfully Deployed! ===")
    print("All abstract patterns working together harmoniously!")


if __name__ == "__main__":
    main()
