"""Module defining the ArtifactCard class for artifact cards in DataDeck."""

from ex0.Card import Card


class ArtifactCard(Card):
    """
    Clase concreta que representa una carta de
    artefacto en el sistema DataDeck.
    Los artefactos son modificadores
    permanentes en el juego con una durabilidad específica.
    """

    def __init__(self, name: str, cost: int,
                 rarity: str, durability: int, effect: str) -> None:
        """
        Inicializa una carta de artefacto con atributos específicos.

        :param name: Nombre de la carta.
        :param cost: Costo de maná para jugar la carta.
        :param rarity: Rareza de la carta.
        :param durability: Durabilidad del artefacto.
        :param effect: Descripción del efecto del artefacto.
        """
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        """
        Juega la carta de artefacto, aplicando su efecto al estado del juego.

        :param game_state: Estado actual del juego.
        :return: Resultado de jugar la carta.
        """
        if game_state["mana"] < self.cost:
            return {
                'card_played': None,
                'mana_used': 0,
                'effect': "Not enough mana"
            }

        game_state["mana"] -= self.cost
        return {
            'card_played': self.name,
            'mana_used': self.cost,
            'effect': self.activate_ability()["description"]
        }

    def activate_ability(self) -> dict:
        """
        Activa la habilidad del artefacto y devuelve su descripción.

        :return: Diccionario con la descripción del efecto del artefacto.
        """
        return {
            "description": f"Permanent: {self.effect}"
        }
