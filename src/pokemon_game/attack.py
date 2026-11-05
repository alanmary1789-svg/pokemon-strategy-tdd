from pokemon_game.pokemon_type import PokemonType

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
     )

        defender.take_damage(damage)