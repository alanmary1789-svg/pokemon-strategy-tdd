from pokemon_game.attack import Attack
from pokemon_game.battle import Battle
from pokemon_game.damage_calculator import DamageCalculator
from pokemon_game.game import Game
from pokemon_game.player import Player
from pokemon_game.pokemon import Pokemon
from pokemon_game.pokemon_type import PokemonType
from pokemon_game.potion import Potion
from pokemon_game.weather import Weather
from pokemon_game.terrain import Terrain
from pokemon_game.computer_player import ComputerPlayer
from pokemon_game.difficulty_selector import choose_difficulty


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

strategy = choose_difficulty()

player2 = ComputerPlayer(
    "Adversaire",
    charmander,
    strategy,
    [Potion("Potion", 20)]
)

battle = Battle(
    DamageCalculator(),
    weather=Weather.CLEAR,
    terrain=Terrain.NORMAL
)

game = Game(player1, player2, battle)

game.play()