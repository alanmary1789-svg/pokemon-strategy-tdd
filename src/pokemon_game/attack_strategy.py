from abc import ABC, abstractmethod
import random


class AttackStrategy(ABC):

    @abstractmethod
    def choose_attack(self, pokemon, oppenent, battle):
        pass


class RandomAttackStrategy(AttackStrategy):

    def choose_attack(self, pokemon, opponent, battle):
        return random.choice(pokemon.attacks)

class StrongestAttackStrategy(AttackStrategy):

    def choose_attack(self, pokemon, opponent, battle):
        return max(
            pokemon.attacks,
            key=lambda attack: attack.damage
        )

class EffectiveAttackStrategy(AttackStrategy):

    def choose_attack(self, pokemon, opponent, battle):
        return max(
            pokemon.attacks,
            key=lambda attack: battle.calculate_damage(
                pokemon,
                opponent,
                attack
            )
        )
    