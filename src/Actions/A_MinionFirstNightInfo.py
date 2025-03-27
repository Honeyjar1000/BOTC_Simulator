from src.Actions.Action import Action
from src.Utils.FindPlayer import CheckIfCharacterInPlay, GetDemonPlayer, GetMinionPlayers
from src.Utils.ActionOutputData import ActionOutputData
from src.Characters.EnumCharacter import Characters

class A_MinionFirstNightInfo(Action):
    
    def __init__(self, players):
        self.player_minions = GetMinionPlayers(players)
        self.player_demon = GetDemonPlayer(players)

    def __str__(self):
        return "[Minion First Night Info]"

    @staticmethod
    def GetMinionPlayers(players):
        player_minions = []
        minions = [Characters.POISONER, Characters.BARON, Characters.SPY, Characters.SCARLET_WOMAN]
        for minion in minions:
            b_in_play, player = CheckIfCharacterInPlay(minion, players)
            if b_in_play:
                player_minions.append(player)
        return player_minions
    

    
    def TakeAction(self, story_teller, player):
        action_output = ActionOutputData()
        action_output.data['demon_player'] = self.player_demon
        action_output.data['minion_players'] = self.player_minions
        return action_output