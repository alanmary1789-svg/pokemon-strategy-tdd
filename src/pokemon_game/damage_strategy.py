from pokemon_game.pokemon_type import TYPE_EFFECTIVENESS
from abc import ABC, abstractmethod


class DamageStrategy(ABC):
    @abstractmethod

    def calculate(self, attack, attacker, defender):
        pass

class TypeDamageStrategy(DamageStrategy):
    def calculate(self, attack, attacker, defender):
        if defender.type in TYPE_EFFECTIVENESS[attack.type]:
            return attack.damage * TYPE_EFFECTIVENESS[attack.type][defender.type]
        else :
            return attack.damage


class SimpleDamageStrategy(DamageStrategy):
    def calculate(self, attack, attacker, defender):
        return attack.damage

    