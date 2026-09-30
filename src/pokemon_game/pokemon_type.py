from enum import Enum 

class PokemonType(Enum):
    FIRE = "fire"
    WATER = "water"
    GRASS = "grass"
    ELECTRIC = "electric"




TYPE_EFFECTIVENESS = {
    PokemonType.FIRE: {
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 2.0,
    },
    PokemonType.WATER: {
        PokemonType.FIRE: 2.0,
        PokemonType.WATER: 0.5,
        PokemonType.GRASS: 0.5,
    },
    PokemonType.GRASS: {
        PokemonType.FIRE: 0.5,
        PokemonType.WATER: 2.0,
        PokemonType.GRASS: 0.5,
    },
    PokemonType.ELECTRIC: {
        PokemonType.WATER: 2.0,
        PokemonType.GRASS: 0.5,
        PokemonType.ELECTRIC: 0.5,
    },
}