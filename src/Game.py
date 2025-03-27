from src.StoryTeller.StoryTeller import StoryTeller
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.SimVisualiser.GameVisualiser import GameVisualiser
import time
import pygame

class Game:

    def __init__(self, script='TB', player_count=12, player_names=None):

        # Important Variables
        self.script = script
        self.player_count = player_count
    
        # Create Players - NAMES MUST BE UNIQUE
        self.players = {} # Dictionary of player names - player object
        player_name_arr = []
        if player_names is None:
            for _ in range(self.player_count):
                player_name_arr.append(f'Player {_+1}')
        else:
            for player_name in range(player_names):
                player_name_arr.append(player_name)
        random.shuffle(player_name_arr)
        for name in player_name_arr:
            self.players[name] = 0
        
        # Story Teller
        self.story_teller = StoryTeller(self.players, self.script, self.player_count)
        
        # VIsualiser component
        self.game_visualiser = None

    def GenerateGame(self):
        if self.script == "TB":
            character_type_dist = GetBaseCharacterTypeDistribution(self.player_count)
            character_list, self.story_teller.black_board.demon_bluffs = GetRandomCharactersAndBluffsTB(character_type_dist)
            self.players = CreatePlayers(character_list, self.players)
            self.PrintPlayers(self.players, self.story_teller.black_board.demon_bluffs)
            self.game_visualiser = GameVisualiser(players=self.players, story_teller=self.story_teller)
            self.game_visualiser.initialize_display()
            self.game_visualiser.update_display()


    def RunGame(self):
        clock = pygame.time.Clock()  # To limit FPS
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False  # Exit the loop when the window is closed
            
            self.story_teller.tick()
            self.game_visualiser.update_display()
            clock.tick(60)  # 60 FPS

        pygame.quit()  # Quit pygame properly

            
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