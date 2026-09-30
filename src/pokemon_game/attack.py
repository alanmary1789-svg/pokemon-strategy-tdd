from pokemon_game.pokemon_type import PokemonType

class Attack:
    type : PokemonType

    def __init__(self, name : str, damage : int, attack_type : PokemonType):
        self.name = name 
        self.damage = damage
        self.type = attack_type 

