import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB

# Define a simple action node
class NodeST_CallTownSquare(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_CallTownSquare, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Set Town Square
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        self.black_board.b_in_townsquare = True

        return py_trees.common.Status.SUCCESS
        