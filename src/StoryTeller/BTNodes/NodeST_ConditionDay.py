import py_trees
from src.StoryTeller.StoryTellerBB import StoryTellerBB

# Define a simple action node
class NodeST_ConditionDay(py_trees.behaviour.Behaviour):
    def __init__(self, name, black_board:StoryTellerBB):
        self.black_board = black_board
        super(NodeST_ConditionDay, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's Day
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")
        condition = False
        if (self.black_board.b_is_day == True) and (self.black_board.b_in_townsquare == False):
            condition = True

        if condition:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE
        