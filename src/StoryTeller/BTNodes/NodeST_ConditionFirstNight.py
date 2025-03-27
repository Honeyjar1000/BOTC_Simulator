import py_trees

# Define a simple action node
class NodeST_ConditionFirstNight(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_ConditionFirstNight, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     Check if it's the first night
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")

        if self.story_teller.black_board.b_first_night == True:
            return py_trees.common.Status.SUCCESS
        else:
            return py_trees.common.Status.FAILURE
        