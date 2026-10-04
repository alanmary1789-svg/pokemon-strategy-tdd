from pokemon_game.pokemon_type import TYPE_EFFECTIVENESS
from pokemon_game.weather import WEATHER_EFFECTIVENESS
from abc import ABC, abstractmethod


class DamageStrategy(ABC):
    @abstractmethod

    def calculate(self, attack, attacker, defender, context):
        pass

class ContextDamageStrategy(DamageStrategy):
    def calculate(self, attack, attacker, defender, context):
        type_multiplier = TYPE_EFFECTIVENESS[attack.type].get(defender.type, 1)

        weather_multiplier = WEATHER_EFFECTIVENESS[context.weather].get(attack.type, 1)

        return attack.damage * type_multiplier * weather_multiplier 


class SimpleDamageStrategy(DamageStrategy):
    def calculate(self, attack, attacker, defender, context):
        return attack.damage

    