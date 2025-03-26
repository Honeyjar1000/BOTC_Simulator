import py_trees
from src.Utils.CharacterTypeDistribution import *
from src.Utils.CreatePlayers import *
from src.Characters import *
from src.Actions import *
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_DemonFirstNightInfo import A_DemonFirstNightInfo


# Define a simple action node
class NodeST_DemonFirstNightInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_DemonFirstNightInfo, self).__init__(name)

    def update(self):
        
        ###########################################
        ###########################################
        ###
        ###     Demon Starting Info
        ###
        ###########################################
        ###########################################

        #print(f"Executing: {self.name}")
        print("\nStoryteller gives demon info...")
        _, imp_player = CheckIfCharacterInPlay(Characters.IMP, self.black_board.players)
        print(f'\nStory teller thinks about waking up {imp_player.player_name}, the Imp to give them beginning info' )

        action = A_DemonFirstNightInfo(self.black_board.players, self.black_board.demon_bluffs)
        imp_player.WakeAtNight(action)
        imp_player.bb.print_beliefs()


        return py_trees.common.Status.SUCCESS