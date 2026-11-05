from pokemon_game.attack import Attack
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.damage_context import DamageContext
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.weather import Weather
from pokemon_game.terrain import Terrain


def test_damage_calculator_applies_all_modifiers():
    calculator = DamageCalculator()

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC
    )

    squirtle = Pokemon(
        "Squirtle",
        100,
        PokemonType.WATER
    )

    thunderbolt = Attack(
        "Thunderbolt",
        20,
        PokemonType.ELECTRIC
    )

    context = DamageContext(
        weather=Weather.RAIN,
        terrain=Terrain.ELECTRIC
    )

    damage = calculator.calculate(
        thunderbolt,
        pikachu,
        squirtle,
        context
    )

    assert damage == 60