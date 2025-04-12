import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_UndertakerMove import A_UndertakerMove

# Define a simple action node
class NodeST_UndertakerMoves(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_UndertakerMoves, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Poisoner wakes up and poisons
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, undertaker_player = CheckIfCharacterInPlay(Characters.UNDERTAKER, self.story_teller.black_board.players)
        if b_in_play and undertaker_player.alive:
            action = A_UndertakerMove(self.story_teller.black_board.players)
            undertaker_player.WakeAtNight(story_teller=self.story_teller, action=action)
            undertaker_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        