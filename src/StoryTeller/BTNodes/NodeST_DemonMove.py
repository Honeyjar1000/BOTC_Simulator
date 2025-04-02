import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import GetDemonPlayers
from src.Characters.EnumCharacter import Characters
from src.Actions.A_ImpMove import A_ImpMove

# Define a simple action node
class NodeST_DemonMove(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_DemonMove, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Poisoner wakes up and poisons
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        # Note there can by multiple imps, find the alive one...
        demon_players = GetDemonPlayers(self.story_teller.black_board.players)
        for demon_player in demon_players:
            if demon_player.alive:
                action = A_ImpMove(self.story_teller.black_board.players)
                demon_player.WakeAtNight(story_teller=self.story_teller, action=action)
                demon_player.bb.print_beliefs()
            return py_trees.common.Status.SUCCESS
            