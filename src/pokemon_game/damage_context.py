from pokemon_game.weather import Weather 
from pokemon_game.terrain import Terrain

class DamageContext:

    def __init__(self, weather : Weather = Weather.CLEAR, terrain : Terrain = Terrain.NORMAL):
        self.weather = weather 
        self.terrain = terrain 

