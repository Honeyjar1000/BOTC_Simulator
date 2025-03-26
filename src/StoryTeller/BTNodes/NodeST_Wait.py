import time
import py_trees

class NodeST_Wait(py_trees.behaviour.Behaviour):
    def __init__(self, name, duration):
        self.duration = duration
        self.start_time = None  # To store the start time of the wait
        self.first_enter = True
        super(NodeST_Wait, self).__init__(name)
        

    def update(self):
        """ Update function to check if the wait time has elapsed. """

        if self.first_enter:
            self.first_enter = False
            # This is the first time the node is ticked, so we start the timer
            self.start_time = time.time()
            #print(f"Started waiting for {self.duration} seconds...")

        # Check if the time has elapsed
        if time.time() - self.start_time >= self.duration:
            #print(f"Waited for {self.duration} seconds, proceeding to next node.")
            self.first_enter = True
            return py_trees.common.Status.SUCCESS  # Return SUCCESS when wait is done
        else:
            return py_trees.common.Status.RUNNING  # Still waiting, continue to run the main loop
