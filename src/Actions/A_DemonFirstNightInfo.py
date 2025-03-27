from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Utils.FindPlayer import GetMinionPlayers, GetDemonPlayer

class A_DemonFirstNightInfo(Action):
    
    def __init__(self, players, demon_bluffs):
        self.player_minions = GetMinionPlayers(players)
        self.demon_bluffs = demon_bluffs
        self.demon_player = GetDemonPlayer(players)

    def __str__(self):
        return "[Demon First Night Info]"

    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data['minion_players'] = self.player_minions
        action_output.data['demon_bluffs'] = self.demon_bluffs
        action_output.data['demon_player'] = self.demon_player
        return action_output

