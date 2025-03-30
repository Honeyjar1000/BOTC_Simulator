from src.Actions.Action import Action
from src.Utils.FindPlayer import FindInvestigatorPings
from src.Utils.ActionOutputData import ActionOutputData

class A_InvestigatorInfo(Action):
    
    def __init__(self, players):
        self.investigator_info, self.grim_tokens = FindInvestigatorPings(players)
        return

    def __str__(self):
        return "[Investigator Info]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data["investigator_info"] = self.investigator_info
        story_teller.black_board.grimoir.data.data["investigator_info_correct"] = self.grim_tokens[0]
        story_teller.black_board.grimoir.data.data["investigator_info_wrong"] = self.grim_tokens[1]
        return action_output