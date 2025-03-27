import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_PoisonerMove import A_PoisonerMove

# Define a simple action node
class NodeST_PoisonerMove(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_PoisonerMove, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Poisoner wakes up and poisons
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, poisoner_player = CheckIfCharacterInPlay(Characters.POISONER, self.story_teller.black_board.players)
        if b_in_play:
            action = A_PoisonerMove(self.story_teller.black_board.players)
            poisoner_player.WakeAtNight(story_teller=self.story_teller, action=action)
            poisoner_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        