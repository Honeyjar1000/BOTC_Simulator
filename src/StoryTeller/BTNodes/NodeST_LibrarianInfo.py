import py_trees
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_LibrarianInfo import A_LibrarianInfo

# Define a simple action node
class NodeST_LibrarianInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
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
        
        b_in_play, librarian_player = CheckIfCharacterInPlay(Characters.LIBRARIAN, self.story_teller.black_board.players)
        if b_in_play and librarian_player.alive:
            action = A_LibrarianInfo(self.story_teller.black_board.players)
            librarian_player.WakeAtNight(story_teller=self.story_teller, action=action)
            librarian_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        