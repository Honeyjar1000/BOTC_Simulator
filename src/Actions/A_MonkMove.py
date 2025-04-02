from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData

class A_MonkMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Poisoner Moves]"

    def TakeAction(self, story_teller, player):
        # Unprotect all players

        player = player.brain.think_pick_player()
        player.b_is_monk_protected = True
        action_output = ActionOutputData()
        action_output.data["monk_protects"] = player
        story_teller.black_board.grimoir.data.data["monk_protects"] = player     # Repeat for everything that would have a reminder token
        return action_output