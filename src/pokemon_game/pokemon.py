from pokemon_game.pokemon_type import PokemonType
from pokemon_game.damage_strategy import DamageStrategy

class Pokemon:
    hp : int 
    type : PokemonType

    def __init__(self, name : str, max_hp : int, pokemon_type : PokemonType):
        self.max_hp = max_hp
        self.name = name 
        self.hp = max_hp
        self.type = pokemon_type    

    def take_damage(self, damage : int):
        if self.hp > damage :
            self.hp -= damage
        else : 
            self.hp = 0


    def is_ko(self):
        return self.hp == 0 

    def heal(self, amount):
        self.hp += amount
        if self.hp > self.max_hp :
            self.hp = self.max_hp 
    """
    def attack(self, target, attack, damage_strategy : DamageStrategy):
        damage = damage_strategy.calculate(attack, self, target)
        target.take_damage(damage)
    """
