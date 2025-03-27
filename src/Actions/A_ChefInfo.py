from src.Actions.Action import Action
from src.Utils.FindPlayer import GetChefNumber
from src.Utils.ActionOutputData import ActionOutputData

class A_ChefInfo(Action):
    
    def __init__(self, players):
        self.chef_info = GetChefNumber(players)
        return

    def __str__(self):
        return "[Chef Info]"

    def TakeAction(self):
        action_output = ActionOutputData()
        action_output.data["chef_info"] = self.chef_info
        return action_output