from pokemon_game.damage_strategy import DamageStrategy
from pokemon_game.weather import Weather
from pokemon_game.damage_context import DamageContext
from pokemon_game.damage_strategy import DamageStrategy 


class Battle:
    def __init__(self, damage_strategy : DamageStrategy, weather : Weather = Weather.CLEAR): 
        self.damage_strategy = damage_strategy
        self.weather = weather


    def attack(self, attacker, defender, attack):
        context = DamageContext(self.weather)

        damage = self.damage_strategy.calculate(attack, attacker, defender, context)

        defender.take_damage(damage)