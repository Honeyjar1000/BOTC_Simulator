import py_trees
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.Characters import *
from src.Actions import *

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


# Define a simple action node
class NodeStoryTellerNightTime(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board):
        self.black_board = black_board
        super(NodeStoryTellerNightTime, self).__init__(name)

    def update(self):
        #print(f"Executing: {self.name}")

        if self.black_board.b_in_night_phase == False:
            return py_trees.common.Status.SUCCESS

        self.black_board.night_count += 1

        #print(f'\nRunning night {self.night_count}')

        ##################################################
        ##################################################
        if self.black_board.night_count == 1:
            
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
                b_in_play, current_player = CheckIfCharacterInPlay(minion, self.black_board.players)
                if b_in_play:
                    print(f'\nStory Teller wakes up {current_player.player_name}, the {str(current_player.character)} to learn starting Minion Info')
                    action = A_MinionFirstNightInfo(self.black_board.players)
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
            _, imp_player = CheckIfCharacterInPlay(C_Imp, self.black_board.players)
            print(f'\nStory teller thinks about waking up {imp_player.player_name}, the Imp to give them beginning info' )
            action = A_DemonFirstNightInfo(self.black_board.players)
            imp_player.WakeAtNight(action)
            imp_player.bb.print_beliefs()

            ###########################################
            ###########################################
            ###
            ###     Other First Night Info
            ###
            ###########################################
            ###########################################
            for c in self.black_board.first_night_order:
                b_character_in_play, current_player = CheckIfCharacterInPlay(c, self.black_board.players) # type: ignore
                if b_character_in_play:
                    print(f'\nStory Teller thinks about waking up {current_player.player_name}, the {str(current_player.character)}')
                    #current_player.WakeAtNight()
                    
        ##################################################
        ##################################################

        # Wake up minions

        # Wake up demon

        # Wake up everyone else


        return py_trees.common.Status.SUCCESS