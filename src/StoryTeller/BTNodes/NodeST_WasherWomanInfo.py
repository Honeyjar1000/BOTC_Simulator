import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman
from src.Actions.A_WashWomanInfo import A_WashWomanInfo

# Define a simple action node
class NodeST_WasherWomanInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_WasherWomanInfo, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, washer_woman_player = CheckIfCharacterInPlay(C_WasherWoman, self.black_board.players)
        if b_in_play:
            action = A_WashWomanInfo(self.black_board.players)
            washer_woman_player.WakeAtNight(action)
            washer_woman_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        