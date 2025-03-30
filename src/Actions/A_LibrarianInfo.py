from src.Actions.Action import Action
from src.Utils.FindPlayer import FindLibrarianPings
from src.Utils.ActionOutputData import ActionOutputData

class A_LibrarianInfo(Action):
    
    def __init__(self, players):
        self.librarian_info, self.grim_tokens = FindLibrarianPings(players)
        return

    def __str__(self):
        return "[Librarian Info]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data["librarian_info"] = self.librarian_info
        story_teller.black_board.grimoir.data.data["librarian_info_correct"] = self.grim_tokens[0]
        story_teller.black_board.grimoir.data.data["librarian_info_wrong"] = self.grim_tokens[1]
        return action_output