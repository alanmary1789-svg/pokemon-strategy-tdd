from pokemon_game.weather import Weather 

class DamageContext:

    def __init__(self, weather : Weather = Weather.CLEAR):
        self.weather = weather 


