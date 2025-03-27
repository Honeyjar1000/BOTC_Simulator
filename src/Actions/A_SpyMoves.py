from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Utils.FindPlayer import GetNeighbours, CheckPlayerAlignment

class A_SpyMoves(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Spy Moves]"

    def TakeAction(self, story_teller, player):

        action_output = ActionOutputData()
        action_output.data["spy_info"] = "DO LATER"
        return action_output