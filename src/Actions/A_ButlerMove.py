from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData

class A_ButlerMove(Action):
    
    def __init__(self, players):
        self.players = players
        self.poisoner_hits = None
        return

    def __str__(self):
        return "[Butler Moves]"

    def TakeAction(self, story_teller, player):
        # Unpoison all players?

        picked_player = player.brain.think_pick_player_not_self(player)
        action_output = ActionOutputData()
        action_output.data["butler_picks"] = picked_player
        return action_output