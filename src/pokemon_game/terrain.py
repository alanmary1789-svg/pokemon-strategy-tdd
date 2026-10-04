from enum import Enum
from pokemon_game.pokemon_type import PokemonType

class Terrain(Enum):
    NORMAL = "normal"
    GRASSY = "grassy"
    ELECTRIC = "electric"

TERRAIN_EFFECTIVENESS = {
    Terrain.NORMAL: {},
    Terrain.GRASSY: {
        PokemonType.GRASS: 1.5,
    },
    Terrain.ELECTRIC: {
        PokemonType.ELECTRIC: 1.5,
    },
}