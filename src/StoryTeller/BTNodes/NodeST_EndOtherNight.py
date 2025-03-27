import py_trees

# Define a simple action node
class NodeST_EndOtherNight(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_EndOtherNight, self).__init__(name)

    def update(self):
            
        ###########################################
        ###########################################
        ###
        ###     End other nights, change some var
        ###
        ###########################################
        ###########################################
        #print(f"Executing: {self.name}")

        self.story_teller.black_board.b_in_night_phase = False
        self.story_teller.black_board.b_is_day = True

        return py_trees.common.Status.SUCCESS
        