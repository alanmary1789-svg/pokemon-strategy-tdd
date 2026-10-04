from pokemon_game.pokemon_type import PokemonType
from pokemon_game.damage_context import DamageContext
from pokemon_game.damage_strategy import DamageStrategy 

class Attack:
    type : PokemonType

    def __init__(self, name : str, damage : int, attack_type : PokemonType):
        self.name = name 
        self.damage = damage
        self.type = attack_type 

    def attack(self, attacker, defender, attack):

        damage = self.damage_strategy.calculate(
        attack,
        attacker,
        defender,
        context
     )

        defender.take_damage(damage)