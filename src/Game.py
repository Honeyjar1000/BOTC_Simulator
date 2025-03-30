from src.StoryTeller.StoryTeller import StoryTeller
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.SimVisualiser.GameVisualiser import GameVisualiser
import time
import pygame

class Game:

    def __init__(self, script='TB', player_count=12, player_names=None, wait_duration=1):

        # Important Variables
        self.player_names = player_names
        self.script = script
        self.player_count = player_count
        self.wait_duration = wait_duration
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
        self.story_teller = StoryTeller(self.players, self.script, self.player_count, self.wait_duration)
        
        # VIsualiser component
        self.game_visualiser = None

    def GenerateGame(self):
        if self.script == "TB":
            character_type_dist = GetBaseCharacterTypeDistribution(self.player_count)
            character_list, self.story_teller.black_board.demon_bluffs = GetRandomCharactersAndBluffsTB(character_type_dist)
            self.players = CreatePlayers(character_list, self.players)
            self.story_teller.PickRedHerring()
            self.story_teller.black_board.grimoir.data.data["demon_bluffs"] = self.story_teller.black_board.demon_bluffs
            self.story_teller.black_board.grimoir.assign_player_characters(self.players)
            self.PrintPlayers(self.players, self.story_teller.black_board.demon_bluffs, self.story_teller.black_board.grimoir.data.data['red_herring'])
            self.game_visualiser = GameVisualiser(players=self.players, story_teller=self.story_teller)
            self.game_visualiser.initialize_display()
            self.game_visualiser.update_display()


    def RunGame(self):
        clock = pygame.time.Clock()
        running = True
        game_over = False  # Flag to pause game logic after win

        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_r:
                        self.RestartGame()
                        game_over = False  # Reset pause flag

            if not game_over:
                self.story_teller.tick()
                result = self.CheckWinCondition()
                if result:
                    print("Game Over.")
                    game_over = True

            # Always redraw the display, even if paused
            self.game_visualiser.update_display()
            clock.tick(60)

        pygame.quit()



    def RestartGame(self):
        # Here we reset or re-initialize the necessary components for restarting the game.
        print("Restarting the game...")

                # Create Players - NAMES MUST BE UNIQUE
        self.players = {} # Dictionary of player names - player object
        player_name_arr = []
        if self.player_names is None:
            for _ in range(self.player_count):
                player_name_arr.append(f'Player {_+1}')
        else:
            for player_name in range(self.player_names):
                player_name_arr.append(player_name)
        random.shuffle(player_name_arr)
        for name in player_name_arr:
            self.players[name] = 0
        
        # Story Teller
        self.story_teller = StoryTeller(self.players, self.script, self.player_count, self.wait_duration)
        
        # VIsualiser component
        self.game_visualiser = None

        self.GenerateGame()  # You can re-call the game generation logic


    def CheckWinCondition(self):
        alive_players = [p for p in self.players.values() if p.alive]
        alive_count = len(alive_players)

        demon_player = next((p for p in self.players.values() if p.character.character_type == "Demon"), None)

        if demon_player is None:
            return None  # Safety check
        if not demon_player.alive:
            print("\n🎉 Good wins! The demon is dead.\n")
            return "GOOD"
        if alive_count == 2:
            if demon_player in alive_players:
                print("\n😈 Evil wins! Only two players left and the demon survives.\n")
                return "EVIL"
        if self.story_teller.black_board.b_saint_executed:
            print("\n😈 Evil wins! the saint has been executed.\n")
            return "EVIL"
        return None



            
    @staticmethod
    def PrintCharacters(character_list):
        s = 'Characters: : '
        for c in character_list:
            s += str(c) + " "
        print(s)
    
    @staticmethod
    def PrintPlayers(player_dict, demon_bluffs, red_herring):
        s = '\n---------------------------------------------------\n\n'
        s += 'Players:\n\n'
        for (i, key) in enumerate(player_dict):
            s+= f'{key} is the {player_dict[key].character.character_name}\n'
        s += "\nDemon Bluffs:\n"
        for demon_bluff in demon_bluffs:
            s += "\n" + str(demon_bluff)
        if (red_herring != None):
            s += f'\n\n{red_herring} is the Red Herring\n'
        s+='\n\n---------------------------------------------------\n'
        print(s)

    