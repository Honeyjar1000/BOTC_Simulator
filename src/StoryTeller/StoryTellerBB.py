from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.Characters import *
from src.Actions import *

class StoryTellerBB:
    def __init__(self, players, scipt, player_count):
        self.script = scipt # Script
        self.player_count = player_count    # Number of Player
        self.demon_bluffs = []  # Demon Bluffs
        self.first_night_order, self.other_night_order = GetCharacterNightOrder(self.script) # Night Character Order
        self.night_count = 0    # Night Count
        self.game_over = False  # Game over condition
        self.players = players # Dictionary of player names - player object 
        self.b_in_night_phase = True    # In night phase - initialised as True
        self.b_first_night = True
        self.b_is_day = False
        self.b_in_townsquare = False
        self.red_herring = None
