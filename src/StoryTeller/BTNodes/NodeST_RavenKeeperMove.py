import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Utils.FindPlayer import CheckIfCharacterInPlay
from src.Characters.EnumCharacter import Characters
from src.Actions.A_RavenKeeperMove import A_RavenKeeperMove

# Define a simple action node
class NodeST_RavenMove(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_RavenMove, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Monk wakes up and protects
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        
        b_in_play, raven_keeper_player = CheckIfCharacterInPlay(Characters.RAVEN_KEEPER, self.story_teller.black_board.players)
        if b_in_play and (not raven_keeper_player.alive):
            if (raven_keeper_player.character.used == False):
                raven_keeper_player.character.used = True
                action = A_RavenKeeperMove(self.story_teller.black_board.players)
                raven_keeper_player.WakeAtNight(story_teller=self.story_teller, action=action)
                raven_keeper_player.bb.print_beliefs()
        return py_trees.common.Status.SUCCESS
        