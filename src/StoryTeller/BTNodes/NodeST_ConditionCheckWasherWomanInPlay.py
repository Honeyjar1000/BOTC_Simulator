import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman

# Define a simple action node
class NodeST_ConditionCheckWasherWomanInPlay(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_ConditionCheckWasherWomanInPlay, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        condition, person = CheckIfCharacterInPlay(C_WasherWoman, self.black_board.players)
        self.black_board.b_washerwoman_in_play = condition
        return py_trees.common.Status.SUCCESS
        