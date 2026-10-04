from pokemon_game.pokemon import Pokemon
from pokemon_game.attack import Attack
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.damage_strategy import ContextDamageStrategy
from pokemon_game.battle import Battle
from pokemon_game.weather import Weather
from pokemon_game.terrain import Terrain    


def test_battle_applies_damage_strategy():
    charmander = Pokemon("Charmander", 100, PokemonType.FIRE)
    bulbasaur = Pokemon("Bulbasaur", 100, PokemonType.GRASS)
    ember = Attack("Ember", 20, PokemonType.FIRE)

    strategy = ContextDamageStrategy()
    battle = Battle(strategy)

    battle.attack(charmander, bulbasaur, ember)

    assert bulbasaur.hp == 60

def test_battle_has_weather():
    strategy = ContextDamageStrategy()
    battle = Battle(strategy, Weather.RAIN)

    assert battle.weather == Weather.RAIN

def test_battle_has_terrain():
    strategy = ContextDamageStrategy()

    battle = Battle(strategy, terrain=Terrain.GRASSY)

    assert battle.terrain == Terrain.GRASSY

    