from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Utils.FindPlayer import GetNeighbours, CheckPlayerAlignment

class A_UndertakerMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Undertake Moves]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data["player_roles"][story_teller.black_board.executed_today.player_name] = story_teller.black_board.executed_today.character
        return action_output