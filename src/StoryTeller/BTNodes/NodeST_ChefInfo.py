import py_trees
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_ChefInfo import A_ChefInfo

# Define a simple action node
class NodeST_ChefInfo(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_ChefInfo, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, chef_player = CheckIfCharacterInPlay(Characters.CHEF, self.story_teller.black_board.players)
        if b_in_play:
            action = A_ChefInfo(self.story_teller.black_board.players)
            chef_player.WakeAtNight(story_teller=self.story_teller, action=action)
            chef_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        