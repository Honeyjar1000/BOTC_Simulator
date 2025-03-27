import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_ButlerMove import A_ButlerMove

# Define a simple action node
class NodeST_Butler(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_Butler, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Poisoner wakes up and poisons
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, butler_player = CheckIfCharacterInPlay(Characters.BUTLER, self.story_teller.black_board.players)
        if b_in_play:
            action = A_ButlerMove(self.story_teller.black_board.players)
            butler_player.WakeAtNight(story_teller=self.story_teller, action=action)
            butler_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        