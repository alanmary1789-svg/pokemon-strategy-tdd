from pokemon_game.attack import Attack
from pokemon_game.battle import Battle
from pokemon_game.damage_strategy import ContextDamageStrategy
from pokemon_game.game import Game
from pokemon_game.player import Player
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.potion import Potion
from pokemon_game.weather import Weather
from pokemon_game.terrain import Terrain


thunderbolt = Attack(
    "Thunderbolt",
    20,
    PokemonType.ELECTRIC
)

ember = Attack(
    "Ember",
    20,
    PokemonType.FIRE
)

pikachu = Pokemon(
    "Pikachu",
    100,
    PokemonType.ELECTRIC,
    [thunderbolt]
)

charmander = Pokemon(
    "Charmander",
    100,
    PokemonType.FIRE,
    [ember]
)

player1 = Player(
    "Alan",
    pikachu,
    [Potion("Potion", 20)]
)

player2 = Player(
    "Adversaire",
    charmander,
    [Potion("Potion", 20)]
)

battle = Battle(
    ContextDamageStrategy(),
    weather=Weather.CLEAR,
    terrain=Terrain.NORMAL
)

game = Game(player1, player2, battle)

game.play()