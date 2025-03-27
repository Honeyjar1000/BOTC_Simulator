from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Player.PlayerBrain import Brain

class A_PoisonerMove(Action):
    
    def __init__(self, players):
        self.players = players
        self.poisoner_hits = None
        return

    def __str__(self):
        return "[Poisoner Moves]"

    def TakeAction(self, brain:Brain):
        # Unpoison all players?

        player = brain.think_pick_player()
        player.b_is_poisoned = True
        action_output = ActionOutputData()
        action_output.data["poisoner_hits"] = player
        return action_output