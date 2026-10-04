from enum import Enum 
from pokemon_game.pokemon_type import PokemonType, TYPE_EFFECTIVENESS

class Weather(Enum):
    CLEAR = "clear"
    RAIN = "rain"
    SUN = "sun"


WEATHER_EFFECTIVENESS = {
    Weather.RAIN: {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 1.5,
    },
    Weather.SUN: {
        PokemonType.FIRE: 1.5,
        PokemonType.WATER: 0.5,
    },
    Weather.CLEAR: {}
}