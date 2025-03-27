from src.Actions.Action import Action
from src.Utils.FindPlayer import FindWashWomanPings
from src.Utils.ActionOutputData import ActionOutputData

class A_WashWomanInfo(Action):
    
    def __init__(self, players):
        self.washer_woman_info = FindWashWomanPings(players)
        return

    def __str__(self):
        return "[Washer Woman Info]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data["washer_woman_info"] = self.washer_woman_info
        return action_output