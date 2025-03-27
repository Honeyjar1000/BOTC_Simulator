from src.Actions.Action import Action
from src.Utils.FindPlayer import FindInvestigatorPings
from src.Utils.ActionOutputData import ActionOutputData

class A_InvestigatorInfo(Action):
    
    def __init__(self, players):
        self.investigator_info = FindInvestigatorPings(players)
        return

    def __str__(self):
        return "[Investigator Info]"

    def TakeAction(self):
        action_output = ActionOutputData()
        action_output.data["investigator_info"] = self.investigator_info
        return action_output