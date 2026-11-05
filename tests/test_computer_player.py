from pokemon_game.attack import Attack
from pokemon_game.attack_strategy import StrongestAttackStrategy
from pokemon_game.computer_player import ComputerPlayer
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType


def test_computer_player_chooses_attack_using_its_strategy():
    ember = Attack("Ember", 20, PokemonType.FIRE)
    flamethrower = Attack("Flamethrower", 40, PokemonType.FIRE)

    charmander = Pokemon(
        "Charmander",
        100,
        PokemonType.FIRE,
        [ember, flamethrower]
    )

    computer = ComputerPlayer(
        "Adversaire",
        charmander,
        StrongestAttackStrategy()
    )

    chosen_attack = computer.choose_attack(None, None)

    assert chosen_attack is flamethrower

from pokemon_game.attack_strategy import EffectiveAttackStrategy
from pokemon_game.battle import Battle
from pokemon_game.damage_calculator import DamageCalculator

def test_computer_players_use_different_attack_strategies():
    ember = Attack("Ember", 30, PokemonType.FIRE)
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)

    charmander = Pokemon(
        "Charmander",
        100,
        PokemonType.FIRE,
        [ember, thunderbolt]
    )

    squirtle = Pokemon(
        "Squirtle",
        100,
        PokemonType.WATER
    )

    battle = Battle(DamageCalculator())

    medium_computer = ComputerPlayer(
        "Adversaire moyen",
        charmander,
        StrongestAttackStrategy()
    )

    hard_computer = ComputerPlayer(
        "Adversaire difficile",
        charmander,
        EffectiveAttackStrategy()
    )

    assert medium_computer.choose_attack(squirtle, battle) is ember
    assert hard_computer.choose_attack(squirtle, battle) is thunderbolt