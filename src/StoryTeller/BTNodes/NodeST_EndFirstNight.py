import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB

# Define a simple action node
class NodeST_EndFirstNight(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_EndFirstNight, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     End first night, change some var
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        self.black_board.b_in_night_phase = False
        self.black_board.b_first_night = False
        self.black_board.b_is_day = True

        return py_trees.common.Status.SUCCESS
        