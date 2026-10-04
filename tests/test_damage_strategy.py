from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.attack import Attack
from pokemon_game.damage_strategy import DamageStrategy, ContextDamageStrategy, SimpleDamageStrategy
from pokemon_game.damage_context import DamageContext

import pytest

context = DamageContext()

def test_damage_strategy_cannot_be_instantiated():
    with pytest.raises(TypeError):
        DamageStrategy()

def test_resistant_type_halves_attack_damage():
    pikachu = Pokemon("pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("bulbasor", 100, PokemonType.GRASS)
    foudre = Attack("foudre", 20, PokemonType.ELECTRIC)

    strategy = ContextDamageStrategy()

    damage = strategy.calculate(foudre, pikachu, bulbasaur, context)

    assert damage == 10

def test_super_effective_attack_doubles_damage():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)

    ember = Attack("Ember", 20, PokemonType.FIRE)

    strategy = ContextDamageStrategy()
    damage = strategy.calculate(ember, charmander, bulbasaur, context)

    assert damage == 40

def test_neutral_type_keeps_normal_damage():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    pikachu = Pokemon("pikachu", 100, PokemonType.ELECTRIC)

    ember = Attack("Ember", 20, PokemonType.FIRE)
    strategy = ContextDamageStrategy()
    damage = strategy.calculate(ember, charmander, pikachu, context)

    assert damage == 20


def test_simple_damage_strategy_returns_base_damage():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)
    thunder_shock = Attack("Thunder Shock", 20, PokemonType.ELECTRIC)

    strategy = SimpleDamageStrategy()

    damage = strategy.calculate(thunder_shock, pikachu, bulbasaur, context)

    assert damage == 20

