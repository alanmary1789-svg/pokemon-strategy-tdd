from pokemon_game.damage_strategy import DamageStrategy
from pokemon_game.weather import Weather
from pokemon_game.damage_context import DamageContext
from pokemon_game.damage_strategy import DamageStrategy 
from pokemon_game.terrain import Terrain
from pokemon_game.damage_calculator import DamageCalculator


class Battle:
    def __init__(self, damage_calculator : DamageCalculator, weather : Weather = Weather.CLEAR, terrain = Terrain.NORMAL): 
        self.damage_calculator = damage_calculator
        self.weather = weather
        self.terrain = terrain 

    def calculate_damage(self, attacker, defender, attack):
        context = DamageContext(self.weather, self.terrain)

        return self.damage_calculator.calculate(attack, attacker, defender, context) 

    def attack(self, attacker, defender, attack):

        damage = self.calculate_damage(attacker, defender, attack)

        defender.take_damage(damage)