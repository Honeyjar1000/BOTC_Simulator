import py_trees

# Define a simple action node
class NodeST_ConditionDay(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
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
        if (self.story_teller.black_board.b_is_day == True) and (self.story_teller.black_board.b_in_townsquare == False):
            condition = True

        if condition:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE
        