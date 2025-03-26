import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_LibrarianInfo import A_LibrarianInfo

# Define a simple action node
class NodeST_LibrarianInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_LibrarianInfo, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, librarian_player = CheckIfCharacterInPlay(Characters.LIBRARIAN, self.black_board.players)
        if b_in_play:
            action = A_LibrarianInfo(self.black_board.players)
            librarian_player.WakeAtNight(action)
            librarian_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        