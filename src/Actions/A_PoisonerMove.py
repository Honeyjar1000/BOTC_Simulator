from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData

class A_PoisonerMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Poisoner Moves]"

    def TakeAction(self, story_teller, player):
        # Unpoison all players?
        if story_teller.black_board.grimoir.data.data["poisoner_hits"] is not None:
            story_teller.black_board.grimoir.data.data["poisoner_hits"].b_is_poisoned = False
        # also when poisoner moves, unpoison player
        player = player.brain.think_pick_player()
        player.b_is_poisoned = True
        action_output = ActionOutputData()
        action_output.data["poisoner_hits"] = player
        story_teller.black_board.grimoir.data.data["poisoner_hits"] = player     # Repeat for everything that would have a reminder token
        return action_output