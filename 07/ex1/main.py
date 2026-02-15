"""
Este módulo demuestra el funcionamiento del sistema de
construcción de mazos en el proyecto DataDeck.
Incluye ejemplos de creación de cartas de diferentes
tipos, gestión de un mazo y simulación de juego.
"""

from ex1.SpellCard import EffectType, SpellCard
from ex0.CreatureCard import CreatureCard
from ex1.ArtifactCard import ArtifactCard
from ex1.Deck import Deck
from ex0.main import Rarity


# Estado global del juego
game_state = {
    "mana": 10,
    "health": 20,
    "effects": []
}


def main() -> None:
    """
    Función principal que ejecuta la demostración
    del sistema de construcción de mazos.
    Incluye la creación de cartas, adición al mazo,
    y simulación de juego al robar y jugar cartas.
    """
    print("=== DataDeck Deck Builder ===\n")
    print("Building deck with different card types...")
    spell_card = SpellCard("Lightning Bolt", 3,
                           Rarity.COMMON.value, EffectType.DAMAGE.value)
    artifact_card = ArtifactCard("Mana Crystal", 2,
                                 Rarity.RARE.value, 5, "+1 mana per turn")
    spell_card2 = CreatureCard("Fire Dragon", 5, Rarity.COMMON.value, 2, 6)

    # Creación del mazo
    deck = Deck()

    deck.add_card(spell_card)
    deck.add_card(artifact_card)
    deck.add_card(spell_card2)

    # Muestra las stats del deck
    stats = deck.get_deck_stats()
    print("Deck stats:", stats)

    # Robar y jugar cartas
    cards_len = len(deck.cards)
    print("\nDrawing and playing cards:")
    for _ in range(cards_len):
        # Draw and play cards
        drawn_card = deck.draw_card()
        print(f"\nDrew: {drawn_card.name} ({drawn_card.__class__.__name__})")
        play_result = drawn_card.play(game_state)
        print("Play result:", play_result)

    print()
    print("Polymorphism in action: Same interface, different card behaviors!")


if __name__ == "__main__":
    main()
