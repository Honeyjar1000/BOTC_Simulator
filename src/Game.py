from src.StoryTeller import StoryTeller
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *

class Game:

    def __init__(self, script='TB', player_count=10, player_names=None):
        self.script = script
        self.player_count = player_count

        self.players = {} # Dictionary of player names - player object
        if player_names is None:
            for _ in range(self.player_count):
                self.players[f'Player {_+1}'] = 0
        else:
            for player_name in range(player_names):
                self.players[player_name] = 0
        
        self.story_teller = StoryTeller(self.players, self.script, self.player_count)
    
    def GenerateGame(self):
        if self.script == "TB":
            character_type_dist = GetBaseCharacterTypeDistribution(self.player_count)
            character_list, self.demon_bluffs = GetRandomCharactersAndBluffsTB(character_type_dist)
            self.players = CreatePlayers(character_list, self.players)
            self.PrintPlayers(self.players, self.demon_bluffs)


    def RunGame(self):
        while not self.story_teller.CheckGameOver():
            self.story_teller.RunNight()
            self.story_teller.RunDay()
            self.story_teller.RunTownSquare()


    @staticmethod
    def PrintCharacters(character_list):
        s = 'Characters: : '
        for c in character_list:
            s += str(c) + " "
        print(s)
    
    @staticmethod
    def PrintPlayers(player_dict, demon_bluffs):
        s = '\n---------------------------------------------------\n\n'
        s += 'Players:\n\n'
        for (i, key) in enumerate(player_dict):
            s+= f'{key} is the {player_dict[key].character.character_name}\n'
        s += "\nDemon Bluffs:\n"
        for demon_bluff in demon_bluffs:
            s += "\n" + str(demon_bluff)
        s+='\n\n---------------------------------------------------\n'
        print(s)