"""
Módulo que define la clase TournamentCard, una carta especializada
para su uso en torneos. Implementa funcionalidades de combate y ranking.
"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex4.Rankable import Rankable
import random


class TournamentCard(Card, Combatable, Rankable):
    """
    Clase que representa una carta de torneo.
    Hereda de Card, Combatable y Rankable, proporcionando
    estadísticas de combate y capacidades de ranking.
    """

    def __init__(self,
                 name: str,
                 cost: int,
                 rarity: str,
                 damage: int,
                 defense: int,
                 health: int,
                 combat_type: str):
        """
        Inicializa una nueva instancia de TournamentCard con sus atributos.

        Args:
            name (str): Nombre de la carta.
            cost (int): Costo de maná para jugar la carta.
            rarity (str): Rareza de la carta.
            damage (int): Daño que puede infligir.
            defense (int): Defensa contra ataques.
            health (int): Salud total de la carta.
            combat_type (str): Tipo de combate (e.g., Fuego, Hielo).
        """
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.defense = defense
        self.health = health
        self.combat_type = combat_type
        self.spell_effects = []
        self.total_mana = 0
        self.rating = self.calculate_rating()
        self.wins = 0
        self.losses = 0

    def play(self, game_state: dict) -> dict:
        """
        Juega la carta en el estado actual del juego.

        Args:
            game_state (dict): Estado actual del juego.

        Returns:
            dict: Resultado de jugar la carta.
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
            'effect': "Magical effect"
        }

    def attack(self, target: str):
        """
        Realiza un ataque contra un objetivo.

        Args:
            target (str): Nombre del objetivo.

        Returns:
            dict: Detalles del ataque realizado.
        """
        return {
            "attacker": self.name,
            "target": target,
            "damage": self.damage,
            "combat_type": self.combat_type
        }

    def defend(self, incoming_damage: int) -> dict:
        """
        Defiende contra un ataque entrante.

        Args:
            incoming_damage (int): Daño recibido.

        Returns:
            dict: Resultado de la defensa.
        """
        alive = False if incoming_damage > self.defense else True
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.defense,
            "still_alive": alive
        }

    def get_combat_stats(self):
        """
        Devuelve las estadísticas de combate de la carta.

        Returns:
            dict: Estadísticas de combate.
        """
        return {
            "name": self.name,
            "damage": self.damage,
            "defense": self.defense,
            "health": self.health,
            "combat_type": self.combat_type
        }

    def calculate_rating(self) -> int:
        """
        Calcula el puntaje de la carta basado en su desempeño.

        Returns:
            int: Puntaje calculado.
        """
        return random.randint(1, 10)

    def update_wins(self, wins: int) -> None:
        """
        Actualiza el número de victorias de la carta.

        Args:
            wins (int): Número de victorias a añadir.
        """
        self.wins += wins
        self.rating += 10 * wins

    def update_losses(self, losses: int) -> None:
        """
        Actualiza el número de derrotas de la carta.

        Args:
            losses (int): Número de derrotas a añadir.
        """
        self.losses += losses
        self.rating -= 5 * losses

    def get_rank_info(self) -> dict:
        """
        Devuelve información detallada sobre el ranking de la carta.

        Returns:
            dict: Información del ranking.
        """
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses
        }

    def get_tournament_stats(self) -> dict:
        """
        Devuelve estadísticas detalladas de la carta para torneos.

        Returns:
            dict: Estadísticas del torneo.
        """
        return {
            "name": self.name,
            "rating": self.rating,
            "wins": self.wins,
            "losses": self.losses,
            "damage": self.damage,
            "defense": self.defense,
            "health": self.health,
            "combat_type": self.combat_type
        }
