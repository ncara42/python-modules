from abc import ABC, abstractmethod


class Card(ABC):
    """
    Clase abstracta que define la estructura básica de
    una carta en el sistema DataDeck.
    Incluye métodos para jugar una carta, obtener
    información y verificar si es jugable.
    """

    def __init__(self, name: str, cost: int, rarity: str):
        """
        Inicializa una carta con un nombre, costo y rareza.

        :param name: Nombre de la carta.
        :param cost: Costo de maná para jugar la carta.
        :param rarity: Rareza de la carta.
        """
        self.name = name
        self.cost = cost
        self.rarity = rarity

    @abstractmethod
    def play(self, game_state: dict) -> dict:
        """
        Método abstracto que debe ser implementado para
        definir cómo se juega la carta.

        :param game_state: Estado actual del juego.
        :return: Resultado de jugar la carta.
        """
        pass

    def get_card_info(self) -> dict:
        """
        Devuelve la información básica de la carta.

        :return: Diccionario con el nombre, costo y rareza de la carta.
        """
        return {
            'name': self.name,
            'cost': self.cost,
            'rarity': self.rarity
        }

    def is_playable(self, available_mana: int):
        """
        Verifica si la carta se puede jugar con el maná disponible.

        :param available_mana: Cantidad de maná disponible.
        :return: True si la carta es jugable, False en caso contrario.
        """
        return available_mana >= self.cost
