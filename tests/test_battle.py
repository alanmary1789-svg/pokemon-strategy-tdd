from pokemon_game.pokemon import Pokemon
from pokemon_game.attack import Attack
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.battle import Battle
from pokemon_game.weather import Weather
from pokemon_game.terrain import Terrain    


def test_battle_applies_damage():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)
    ember = Attack("Ember", 20, PokemonType.FIRE)

    calculator = DamageCalculator()
    battle = Battle(calculator)

    battle.attack(charmander, bulbasaur, ember)

    assert bulbasaur.hp == 60

def test_battle_has_weather():
    calculator = DamageCalculator()
    battle = Battle(calculator, Weather.RAIN)

    assert battle.weather == Weather.RAIN

def test_battle_has_terrain():
    calculator = DamageCalculator()

    battle = Battle(calculator, terrain=Terrain.GRASSY)

    assert battle.terrain == Terrain.GRASSY

def test_calculate_damage_does_not_modify_defender_hp():
    pikachu = Pokemon("Pikachu", 100, PokemonType.ELECTRIC)
    squirtle = Pokemon("Squirtle", 100, PokemonType.WATER)
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)

    battle = Battle(DamageCalculator())

    damage = battle.calculate_damage(
        pikachu,
        squirtle,
        thunderbolt
    )

    assert damage == 40
    assert squirtle.hp == 100

def test_battle_attack_returns_actual_damage():
    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC
    )

    squirtle = Pokemon(
        "Squirtle",
        15,
        PokemonType.WATER
    )

    thunderbolt = Attack(
        "Thunderbolt",
        20,
        PokemonType.ELECTRIC
    )

    battle = Battle(DamageCalculator())

    damage = battle.attack(
        pikachu,
        squirtle,
        thunderbolt
    )

    assert damage == 15
    assert squirtle.hp == 0