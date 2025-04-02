import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_WashWomanInfo import A_WashWomanInfo

# Define a simple action node
class NodeST_WasherWomanInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
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
        
        b_in_play, washer_woman_player = CheckIfCharacterInPlay(Characters.WASHER_WOMAN, self.story_teller.black_board.players)
        if b_in_play and washer_woman_player.alive:
            action = A_WashWomanInfo(self.story_teller.black_board.players)
            washer_woman_player.WakeAtNight(story_teller=self.story_teller, action=action)
            washer_woman_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        