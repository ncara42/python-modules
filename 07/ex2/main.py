"""
Este módulo demuestra el funcionamiento del
sistema de habilidades en el proyecto DataDeck.
Incluye ejemplos de creación de cartas de
élite y uso de habilidades de combate y magia.
"""

from ex0.Card import Card
from ex0.main import Rarity
from ex2.EliteCard import EliteCard
from ex2.Combatable import Combatable
from ex2.Magical import Magical


def list_methods(obj):
    return [method for method in dir(obj) if not method.startswith("_")]


def main():
    """
    Función principal que ejecuta la demostración del
    sistema de habilidades.
    Incluye la creación de una carta de élite y la
    simulación de sus capacidades.
    """
    game_state = {
        "mana": 20,
        "health": 20
    }

    print("=== DataDeck Ability System ===")
    arcane_attack = EliteCard("Arcane Warrior", 5,
                              Rarity.RARE.name, 10, 3, 20, "melee")

    print("\nEliteCard capabilities:")
    for cls in [Card, Combatable, Magical]:
        print(f"- {cls.__name__}: {list_methods(cls)}")

    print(f"\nPlaying {arcane_attack.name} "
          f"({arcane_attack.__class__.__name__}):\n")
    arcane_attack.play(game_state)

    print("\nMultiple interface implementation succesful!")


if __name__ == "__main__":
    main()
