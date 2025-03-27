import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_InvestigatorInfo import A_InvestigatorInfo

# Define a simple action node
class NodeST_InvestigatorInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_InvestigatorInfo, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, investigator_player = CheckIfCharacterInPlay(Characters.INVESTIGATOR, self.black_board.players)
        if b_in_play:
            action = A_InvestigatorInfo(self.black_board.players)
            investigator_player.WakeAtNight(action)
            investigator_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        