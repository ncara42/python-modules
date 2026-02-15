"""
Este módulo define la clase `EliteCard`,
que combina habilidades de combate y magia.
"""

from ex0.Card import Card
from ex2.Combatable import Combatable
from ex2.Magical import Magical


class EliteCard(Card, Combatable, Magical):
    """
    Clase que representa una carta de élite con habilidades de combate y magia.
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
        Inicializa una carta de élite con atributos específicos.

        :param name: Nombre de la carta.
        :param cost: Costo de maná para jugar la carta.
        :param rarity: Rareza de la carta.
        :param damage: Daño que puede infligir.
        :param defense: Defensa contra ataques.
        :param health: Salud de la carta.
        :param combat_type: Tipo de combate (e.g., "melee").
        """
        super().__init__(name, cost, rarity)
        self.damage = damage
        self.defense = defense
        self.health = health
        self.combat_type = combat_type
        self.spell_effects = []
        self.total_mana = 0

    def play(self, game_state: dict) -> dict:
        """
        Juega la carta de élite, mostrando sus habilidades de combate y magia.

        :param game_state: Estado actual del juego.
        :return: Resultado de jugar la carta.
        """
        print("Combat phase:")
        print(f"Attack result: {self.attack('Enemy')}")
        print(f"Defense result: {self.defend(2)}")

        print("\nMagic phase:")
        print(f"Spell cast: "
              f"{self.cast_spell('Fireball', ['Enemy1', 'Enemy2'])}")
        self.channel_mana(4)
        print(f"Mana channel: {self.channel_mana(3)}")
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

    def attack(self, target: str) -> dict:
        """
        Ataca a un objetivo.

        :param target: El objetivo del ataque.
        :return: Detalles del ataque.
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

        :param incoming_damage: Daño del ataque entrante.
        :return: Detalles de la defensa.
        """
        alive = False if incoming_damage > self.defense else True
        return {
            "defender": self.name,
            "damage_taken": incoming_damage,
            "damage_blocked": self.defense,
            "still_alive": alive
        }

    def get_combat_stats(self) -> dict:
        """
        Obtiene las estadísticas de combate de la carta.

        :return: Estadísticas de combate.
        """
        return {
            "name": self.name,
            "damage": self.damage,
            "defense": self.defense,
            "health": self.health,
            "combat_type": self.combat_type
        }

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        """
        Lanza un hechizo sobre los objetivos seleccionados.

        :param spell_name: Nombre del hechizo.
        :param targets: Lista de objetivos del hechizo.
        :return: Detalles del hechizo lanzado.
        """
        return {
            "caster": self.name,
            "spell": spell_name,
            "targets": targets,
            "mana_used": self.cost
        }

    def channel_mana(self, amount: int) -> dict:
        """
        Canaliza una cantidad de maná.

        :param amount: Cantidad de maná a canalizar.
        :return: Detalles de la canalización de maná.
        """
        self.total_mana += amount
        return {
            "channeled": amount,
            "total_mana": self.total_mana
        }

    def get_magic_stats(self) -> dict:
        """
        Obtiene las estadísticas mágicas de la carta.

        :return: Estadísticas mágicas.
        """
        return {
            "name": self.name,
            "mana": self.total_mana,
            "spell_effects": self.spell_effects
        }
