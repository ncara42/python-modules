from typing import Union
from ex0.Card import Card


class CreatureCard(Card):
    """
    Clase concreta que representa una carta de
    criatura en el sistema DataDeck.
    Hereda de la clase abstracta `Card` e
    incluye atributos adicionales como ataque y salud.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, attack: int, health: int) -> None:
        """
        Inicializa una carta de criatura con atributos específicos.

        :param name: Nombre de la carta.
        :param cost: Costo de maná para jugar la carta.
        :param rarity: Rareza de la carta.
        :param attack: Valor de ataque de la criatura.
        :param health: Valor de salud de la criatura.
        """
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health

    def play(self, game_state: dict) -> dict:
        """
        Juega la carta de criatura, actualizando el estado del juego.

        :param game_state: Estado actual del juego.
        :return: Resultado de jugar la carta.
        """
        play_result = {
            'card_played': None,
            'mana_used': 0,
            'effect': ""
        }

        if game_state['mana'] >= self.cost:
            game_state['mana'] -= self.cost
            play_result['card_played'] = self.name
            play_result['mana_used'] = self.cost
            play_result['effect'] = "Creature summoned to battlefield"

        return play_result

    def get_card_info(self) -> dict:
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity,
            'type': 'Creature',
            'attack': self.attack,
            'health': self.health
        }

    def attack_target(self, target: str) -> dict[str, Union[str, int, bool]]:
        """
        Realiza un ataque a un objetivo específico.

        :param target: Nombre del objetivo a atacar.
        :return: Resultado del ataque.
        """
        return {
            'attacker': self.name,
            'target': target,
            'damage_dealt': self.attack,
            'combat_resolved': True
        }

    def validate_atributes(self) -> bool:
        """
        Valida que los atributos de ataque y salud sean positivos.

        :return: True si los atributos son válidos, False en caso contrario.
        """
        return self.attack > 0 and self.health > 0
