from src.Actions.Action import Action
from src.Utils.FindPlayer import FindWashWomanPings
from src.Utils.ActionOutputData import ActionOutputData
from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp
from src.Utils.ActionOutputData import ActionOutputData

class A_WashWomanInfo(Action):
    
    def __init__(self, players):
        self.washer_woman_info = FindWashWomanPings(players)
        return

    def __str__(self):
        return "[Minion First Night Info]"

    def TakeAction(self):
        action_output = ActionOutputData()
        action_output.data["washer_woman_info"] = self.washer_woman_info
        return action_output