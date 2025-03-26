import py_trees
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.Characters import *
from src.Actions import *
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Actions.A_MinionFirstNightInfo import A_MinionFirstNightInfo
from src.Characters.EnumCharacter import Characters
from time import sleep

# Define a simple action node
class NodeST_MinionFirstNightInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board):
        self.black_board = black_board
        super(NodeST_MinionFirstNightInfo, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Minion Starting Info
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        print("\nStoryteller gives minion info...")
        all_minion_list = [Characters.POISONER, Characters.BARON, Characters.SPY, Characters.SCARLET_WOMAN]
        for minion in all_minion_list:
            b_in_play, current_player = CheckIfCharacterInPlay(minion, self.black_board.players)
            if b_in_play:
                print(f'\nStory Teller wakes up {current_player.player_name}, the {str(current_player.character)} to learn starting Minion Info')
                action = A_MinionFirstNightInfo(self.black_board.players)
                current_player.WakeAtNight(action)
                current_player.bb.print_beliefs()
                sleep(1)

        return py_trees.common.Status.SUCCESS
        