import py_trees

# Define a simple action node
class NodeST_CallTownSquare(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
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
        self.story_teller.black_board.b_in_townsquare = True

        return py_trees.common.Status.SUCCESS
        