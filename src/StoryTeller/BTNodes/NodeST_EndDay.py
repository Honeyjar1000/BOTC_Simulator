import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB

# Define a simple action node
class NodeST_EndDay(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_EndDay, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     End first night, change some var
        ###
        ###########################################
        ###########################################

        #print(f'Executing {self.name}')

        self.story_teller.black_board.b_in_night_phase = True
        self.story_teller.black_board.b_is_day = False
        self.story_teller.black_board.b_in_townsquare = False
        print("Everyone goes to sleep!")
        return py_trees.common.Status.SUCCESS
        