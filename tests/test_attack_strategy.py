from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.attack import Attack
from pokemon_game.attack_strategy import RandomAttackStrategy
from pokemon_game.attack_strategy import StrongestAttackStrategy
from pokemon_game.attack_strategy import EffectiveAttackStrategy
from pokemon_game.battle import Battle
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.weather import Weather



def test_random_strategy_chooses_an_available_attack():
    thunderbolt = Attack(
        "Thunderbolt",
        20,
        PokemonType.ELECTRIC
    )

    quick_attack = Attack(
        "Quick Attack",
        10,
        PokemonType.ELECTRIC
    )

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [thunderbolt, quick_attack]
    )

    strategy = RandomAttackStrategy()

    chosen_attack = strategy.choose_attack(pikachu, None, None)

    assert chosen_attack in pikachu.attacks

def test_strongest_strategy_chooses_highest_base_damage():
    quick_attack = Attack("Quick Attack", 10, PokemonType.ELECTRIC)
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)
    thunder = Attack("Thunder", 35, PokemonType.ELECTRIC)

    pikachu = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [quick_attack, thunderbolt, thunder]
    )

    strategy = StrongestAttackStrategy()

    chosen_attack = strategy.choose_attack(pikachu, None, None)

    assert chosen_attack is thunder

def test_effective_strategy_chooses_attack_with_highest_actual_damage():
    ember = Attack("Ember", 30, PokemonType.FIRE)
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)

    attacker = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [ember, thunderbolt]
    )

    defender = Pokemon(
        "Squirtle",
        100,
        PokemonType.WATER
    )

    battle = Battle(DamageCalculator())
    strategy = EffectiveAttackStrategy()

    chosen_attack = strategy.choose_attack(
        attacker,
        defender,
        battle
    )

    assert chosen_attack is thunderbolt

def test_effective_strategy_does_not_apply_damage():
    ember = Attack("Ember", 30, PokemonType.FIRE)
    thunderbolt = Attack("Thunderbolt", 20, PokemonType.ELECTRIC)

    attacker = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC,
        [ember, thunderbolt]
    )

    defender = Pokemon(
        "Squirtle",
        100,
        PokemonType.WATER
    )

    battle = Battle(DamageCalculator())
    strategy = EffectiveAttackStrategy()

    strategy.choose_attack(attacker, defender, battle)

    assert defender.hp == 100

def test_effective_strategy_considers_weather():
    ember = Attack("Ember", 20, PokemonType.FIRE)
    vine_whip = Attack("Vine Whip", 25, PokemonType.GRASS)

    attacker = Pokemon(
        "Charmander",
        100,
        PokemonType.FIRE,
        [ember, vine_whip]
    )

    defender = Pokemon(
        "Pikachu",
        100,
        PokemonType.ELECTRIC
    )

    battle = Battle(
        DamageCalculator(),
        weather=Weather.SUN
    )

    strategy = EffectiveAttackStrategy()

    chosen_attack = strategy.choose_attack(
        attacker,
        defender,
        battle
    )

    assert chosen_attack is ember