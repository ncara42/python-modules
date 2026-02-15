"""
Módulo que define la clase TournamentPlatform, responsable de gestionar
cartas, partidas y reportes en un torneo.
"""
from ex4.TournamentCard import TournamentCard
import random


class TournamentPlatform:
    """
    Clase que representa la plataforma de torneos. Permite registrar cartas,
    crear partidas, generar reportes y gestionar el ranking de las cartas.
    """

    def __init__(self):
        """
        Inicializa una nueva instancia de TournamentPlatform.
        """
        self.cards: dict[str, TournamentCard] = {}
        self.matches = []
        self.wins = 0
        self.lose = 0

    def register_card(self, card: TournamentCard) -> str:
        """
        Registra una carta en la plataforma de torneos.

        Args:
            card (TournamentCard): Carta a registrar.

        Returns:
            str: ID único asignado a la carta.
        """
        card_id = f"{card.name}_{random.randint(1000, 9999)}"
        print()
        self.cards[card_id] = card
        return card_id

    def create_match(self, card1_id: str, card2_id: str) -> dict:
        """
        Crea una partida entre dos cartas registradas.

        Args:
            card1_id (str): ID de la primera carta.
            card2_id (str): ID de la segunda carta.

        Returns:
            dict: Resultado de la partida, incluyendo ganador y perdedor.
        """
        winner = card1_id if random.randint(1, 2) == 1 else card2_id
        loser = card2_id if card1_id is winner else card1_id
        self.cards[winner].update_wins(1)
        self.cards[loser].update_losses(1)
        match = {
            "winner": winner,
            "loser": loser,
            "winner_rating": self.cards[winner].rating,
            "loser_rating": self.cards[loser].rating
        }

        self.matches.append(match)
        return match

    def get_leaderboard(self) -> list:
        """
        Genera y muestra la tabla de clasificación del torneo.

        Returns:
            list: Lista de partidas jugadas.
        """
        print("Tournament Leaderboard:")
        sorted_cards = sorted(
            self.cards.values(), key=lambda card: card.rating, reverse=True
        )
        for i, card in enumerate(sorted_cards, 1):
            print(f"{i}. {card.name} - Rating: {card.rating} "
                  f"({card.wins} - {card.losses})")
        return self.matches

    def generate_tournament_report(self) -> dict:
        """
        Genera un reporte detallado del torneo.

        Returns:
            dict: Reporte del torneo con estadísticas generales.
        """
        total_rating = 0
        for card in self.cards.values():
            total_rating += card.rating

        avg_rating: float = total_rating / len(self.cards)
        return {
            "total_cards": len(self.cards),
            "matches_played": len(self.matches),
            "avg_rating": avg_rating,
            "platform_status": "active"
        }

    def print_card_info(self, card_id: str) -> None:
        """
        Imprime información detallada de una carta registrada.

        Args:
            card_id (str): ID de la carta.
        """
        card: TournamentCard | None = self.cards.get(card_id)
        if card is None:
            print(f"Card ID {card_id} does not exist.")
            return
        print(f"{card.name} (ID: {card_id})")
        print("- Interfaces: [Card, Combatable, Rankable]")
        print(f"- Rating: {card.rating}")
        print("- Record: 0-0")
