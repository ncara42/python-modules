from ex0 import Card
from ex1.SpellCard import SpellCard
from ex1.ArtifactCard import ArtifactCard
from ex0.CreatureCard import CreatureCard
import random


class Deck:
    """
    Clase que representa un mazo de cartas en el sistema DataDeck.
    Permite gestionar cartas, incluyendo añadir,
    eliminar, barajar y robar cartas.
    """

    def __init__(self) -> None:
        """
        Inicializa un mazo vacío con estadísticas iniciales.
        """
        self.stats = {
            'total_cards': 0,
            'creatures': 0,
            'spells': 0,
            'artifacts': 0,
            'avg_cost': 0.0
        }

        self.cards: list[Card] = []

    def add_card(self, card: Card) -> None:
        """
        Añade una carta al mazo y actualiza las estadísticas.

        :param card: Carta a añadir al mazo.
        """
        if isinstance(card, ArtifactCard):
            self.stats['artifacts'] += 1
        elif isinstance(card, SpellCard):
            self.stats['spells'] += 1
        elif isinstance(card, CreatureCard):
            self.stats['creatures'] += 1
        else:
            raise ValueError("Unsupported card type")

        self.stats['total_cards'] += 1
        self.cards.append(card)

    def remove_card(self, card_name: str) -> bool:
        """
        Elimina una carta del mazo por su nombre.

        :param card_name: Nombre de la carta a eliminar.
        :return: True si la carta fue eliminada, False en caso contrario.
        """
        for card in self.cards:
            if card.name == card_name:
                self.cards.remove(card)
                return True
        return False

    def shuffle(self) -> None:
        """
        Baraja las cartas del mazo de forma aleatoria.
        """
        random.shuffle(self.cards)

    def draw_card(self) -> Card:
        """
        Roba la primera carta del mazo.

        :return: La carta robada.
        """
        return self.cards.pop(0)

    def get_deck_stats(self) -> dict:
        """
        Calcula y devuelve las estadísticas del mazo.

        :return: Diccionario con las estadísticas del mazo.
        """
        total_cost: int = 0
        for card in self.cards:
            total_cost += card.cost

        self.stats["avg_cost"] = round(total_cost / len(self.cards), 2)

        return self.stats
