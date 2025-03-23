from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.Characters import *
from src.Actions import *
import time
from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman
from src.Characters.TownsFolk.C_Librarian import C_Librarian
from src.Characters.TownsFolk.C_Investigator import C_Investigator
from src.Characters.TownsFolk.C_Chef import C_Chef
from src.Characters.TownsFolk.C_Empath import C_Empath
from src.Characters.TownsFolk.C_FortuneTeller import C_FortuneTeller
from src.Characters.TownsFolk.C_Undertaker import C_Undertaker
from src.Characters.TownsFolk.C_Monk import C_Monk
from src.Characters.TownsFolk.C_RavenKeeper import C_RavenKeeper
from src.Characters.TownsFolk.C_Virgin import C_Virgin
from src.Characters.TownsFolk.C_Slayer import C_Slayer
from src.Characters.TownsFolk.C_Soldier import C_Soldier
from src.Characters.TownsFolk.C_Mayor import C_Mayor
from src.Characters.Outsider.C_Butler import C_Butler
from src.Characters.Outsider.C_Saint import C_Saint
from src.Characters.Outsider.C_Recluse import C_Recluse
from src.Characters.Outsider.C_Drunk import C_Drunk
from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp


class StoryTeller:

    #######################################################
    #######################################################
    ###
    ###     This Class will be responsible for alot.
    ###
    #######################################################
    #######################################################

    def __init__(self, players, scipt, player_count):

        self.script = scipt # Script
        self.player_count = player_count    # Number of Player
        self.demon_bluffs = []  # Demon Bluffs
        self.first_night_order, self.other_night_order = GetCharacterNightOrder(self.script) # Night Character Order
        self.night_count = 0    # Night Count
        self.game_over = False  # Game over condition
        self.players = players # Dictionary of player names - player object
    
    def RunNight(self):
        self.night_count += 1
        #print(f'\nRunning night {self.night_count}')

        ##################################################
        ##################################################
        if self.night_count == 1:
            
            ###########################################
            ###########################################
            ###
            ###     Minion Starting Info
            ###
            ###########################################
            ###########################################
            print("\nStoryteller gives minion info...")
            all_minion_list = [C_Poisoner, C_Baron, C_ScarletWoman, C_Spy]
            for minion in all_minion_list:
                b_in_play, current_player = CheckIfCharacterInPlay(minion, self.players)
                if b_in_play:
                    print(f'\nStory Teller wakes up {current_player.player_name}, the {str(current_player.character)} to learn starting Minion Info')
                    action = A_MinionFirstNightInfo(self.players)
                    current_player.WakeAtNight(action)
                    current_player.bb.print_beliefs()

            ###########################################
            ###########################################
            ###
            ###     Demon Starting Info
            ###
            ###########################################
            ###########################################
            print("\nStoryteller gives demon info...")
            _, imp_player = CheckIfCharacterInPlay(C_Imp, self.players)
            print(f'\nStory teller thinks about waking up {imp_player.player_name}, the Imp to give them beginning info' )
            action = A_DemonFirstNightInfo(self.players)
            imp_player.WakeAtNight(action)
            imp_player.bb.print_beliefs()

            ###########################################
            ###########################################
            ###
            ###     Other First Night Info
            ###
            ###########################################
            ###########################################
            for c in self.first_night_order:
                b_character_in_play, current_player = CheckIfCharacterInPlay(c, self.players) # type: ignore
                if b_character_in_play:
                    print(f'\nStory Teller thinks about waking up {current_player.player_name}, the {str(current_player.character)}')
                    #current_player.WakeAtNight()
        ##################################################
        ##################################################

        # Wake up minions

        # Wake up demon

        # Wake up everyone else

        # Arbitrary rule that game lasts 5 nights for now
        if self.night_count > 1e6:
            self.game_over = True
        return

    def RunDay(self):
        #print(f'Running day {self.night_count}')
        # Run Day
        return

    def RunTownSquare(self):
        #print(f'Calling Town Square!')
        # Run Town Square
        #print(f'Everyone goes to sleep!')
        return
        

    def CheckCharacterWake(self, player):
        #print(f'should we wake {player.player_name} the {player.character.character_name}')
        return

    def CheckGameOver(self):
        return self.game_over
