"""
Este módulo demuestra el funcionamiento de la
clase `CreatureCard` en el sistema DataDeck.
Incluye ejemplos de creación, validación y uso de cartas de criatura.
"""

from ex0.CreatureCard import CreatureCard
from enum import Enum


class DataError(Exception):
    """
    Excepción personalizada para errores relacionados
    con datos inválidos en las cartas.
    """
    pass


class Rarity(Enum):
    """
    Enumeración que define los niveles de rareza de las cartas.
    """
    COMMON = "Common"
    RARE = "Rare"
    LEGENDARY = "Legendary"


def main() -> None:
    """
    Función principal que ejecuta la demostración del sistema de cartas.
    Incluye la creación de una carta de criatura, validación de atributos,
    y simulación de juego y combate.
    """
    print("=== DataDeck Card Foundation ===")

    dragon = CreatureCard("Fire Dragon", 5, Rarity.LEGENDARY.value, 7, 5)
    data_card: dict = dragon.get_card_info()

    dragon_game_state = {
        "mana": 11,
        "health": 20
    }

    print("\nTesting Abstract Base Class Design:")
    print("\nCreatureCard Info:")
    print(data_card)
    try:
        if not dragon.validate_atributes():
            raise DataError("Attack and health must be positive integers.")
    except DataError as e:
        print(f"Error: {e}")

    att_state = dragon.play(dragon_game_state)
    att_result = dragon.attack_target('Goblin Warrior')

    if dragon.is_playable(att_state['mana_used']):
        template = "\nPlaying {} with {} mana available:"
        print(template.format(att_state['card_played'],
                              dragon_game_state['mana']))
        print("Playable: True")
        print(f"Play result: {att_state}")

    template = "\n{} attacks {}:"
    print(template.format(att_state['card_played'], att_result['target']))
    print(f"Attacker result: {att_result}")

    # Testeo, no es parte del juego
    print("\nTesting insufficient mana (3 available)")
    print(f"Playable: {dragon.is_playable(3)}")

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
