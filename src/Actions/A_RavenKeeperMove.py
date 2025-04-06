from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData

class A_RavenKeeperMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[RavenKeeper Moves]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        selected_player = player.brain.think_pick_player_not_self(player)
        print(f'{player.player_name} picks {selected_player.player_name}')
        action_output.data["player_roles"][selected_player.player_name] = selected_player.character
        return action_output