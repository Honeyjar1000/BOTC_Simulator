from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Utils.FindPlayer import GetNeighbours, CheckPlayerAlignment

class A_EmpathMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Empath Moves]"

    def TakeAction(self, story_teller, player):

        left_neighbor, right_neighbor = GetNeighbours(self.players, player)
        empath_count = 0
        if CheckPlayerAlignment(left_neighbor):
            empath_count += 1
        if CheckPlayerAlignment(right_neighbor):
            empath_count += 1
             

        action_output = ActionOutputData()
        action_output.data["empath_info"] = empath_count
        return action_output