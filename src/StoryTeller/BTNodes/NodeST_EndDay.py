import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB

# Define a simple action node
class NodeST_EndDay(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
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

        self.black_board.b_in_night_phase = True
        self.black_board.b_is_day = False
        self.black_board.b_in_townsquare = False

        return py_trees.common.Status.SUCCESS
        