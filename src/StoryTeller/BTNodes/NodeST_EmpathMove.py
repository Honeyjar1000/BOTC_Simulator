import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_EmpathMove import A_EmpathMove

# Define a simple action node
class NodeST_EmpathMove(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_EmpathMove, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Poisoner wakes up and poisons
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, empath_player = CheckIfCharacterInPlay(Characters.EMPATH, self.story_teller.black_board.players)
        if b_in_play:
            action = A_EmpathMove(self.story_teller.black_board.players)
            empath_player.WakeAtNight(story_teller=self.story_teller, action=action)
            empath_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        