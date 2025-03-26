from src.Actions.Action import Action
from src.Utils.FindPlayer import FindLibrarianPings
from src.Utils.ActionOutputData import ActionOutputData

class A_LibrarianInfo(Action):
    
    def __init__(self, players):
        self.librarian_info = FindLibrarianPings(players)
        return

    def __str__(self):
        return "[Librarian Info]"

    def TakeAction(self):
        action_output = ActionOutputData()
        action_output.data["librarian_info"] = self.librarian_info
        return action_output