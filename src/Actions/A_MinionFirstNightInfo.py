from src.Actions.Action import Action
from src.Utils.FindPlayer import CheckIfCharacterInPlay, GetDemonPlayer, GetMinionPlayers
from src.Utils.ActionOutputData import ActionOutputData
from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp

class A_MinionFirstNightInfo(Action):
    
    def __init__(self, players):
        self.player_minions = GetMinionPlayers(players)
        self.player_demon = GetDemonPlayer(players)

    def __str__(self):
        return "[Minion First Night Info]"

    def GetMinionPlayers(self, players):
        player_minions = []
        minions = [C_Poisoner, C_Baron, C_Spy, C_ScarletWoman]
        for minion in minions:
            b_in_play, player = CheckIfCharacterInPlay(minion, players)
            if b_in_play:
                player_minions.append(player)
        return player_minions
    

    
    def TakeAction(self):
        action_output = ActionOutputData()
        action_output.data['demon_player'] = self.player_demon
        action_output.data['minion_players'] = self.player_minions
        return action_output