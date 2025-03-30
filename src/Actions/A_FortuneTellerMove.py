from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Utils.FindPlayer import CheckPlayerIsDemonFortuneTeller

class A_FortuneTellerMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Fortune Teller Moves]"

    def TakeAction(self, story_teller, player):

        players = player.brain.think_pick_2_players()
        empath_info = [players, False]
        for player in players:
            if CheckPlayerIsDemonFortuneTeller(player, story_teller.black_board.grimoir.data.data['red_herring']):
                empath_info[1] = True

        action_output = ActionOutputData()
        action_output.data["fortune_teller_info"] = empath_info
        return action_output