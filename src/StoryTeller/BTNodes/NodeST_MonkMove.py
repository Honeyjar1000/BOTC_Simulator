import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_MonkMove import A_MonkMove

# Define a simple action node
class NodeST_MonkMove(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_MonkMove, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Monk wakes up and protects
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, monk_player = CheckIfCharacterInPlay(Characters.MONK, self.story_teller.black_board.players)
        if b_in_play and monk_player.alive:
            action = A_MonkMove(self.story_teller.black_board.players)
            monk_player.WakeAtNight(story_teller=self.story_teller, action=action)
            monk_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        