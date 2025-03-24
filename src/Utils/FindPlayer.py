from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp

def CheckIfCharacterInPlay(character, player_dict):

    ##########################################################
    ##########################################################
    ###
    ###     Inputs
    ###         - character : Class Type of character to find
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - True / False
    ###         - Player in the True case, Player=None in the False case
    ###
    ##########################################################
    ##########################################################

    for (i,key) in enumerate(player_dict):
        player = player_dict[key]
        #print(type(player.character), character)
        if type(player.character) == character:
            return True, player
    return False, None

def GetMinionPlayers(players):

    ##########################################################
    ##########################################################
    ###
    ###     Find all minion players
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - A list of Type<Player> of all minions
    ###
    ##########################################################
    ##########################################################

    player_minions = []
    minions = [C_Poisoner, C_Baron, C_Spy, C_ScarletWoman]
    for minion in minions:
        b_in_play, player = CheckIfCharacterInPlay(minion, players)
        if b_in_play:
            player_minions.append(player)
    return player_minions

def GetDemonPlayer(players):

    ##########################################################
    ##########################################################
    ###
    ###     Find all minion players
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - A list of Type<Player> of all minions
    ###
    ##########################################################
    ##########################################################

    b_in_play, player = CheckIfCharacterInPlay(C_Imp, players)
    if b_in_play:
        return player
    else:
        print("Error: Can't find demon in Utils.FindPlayer.GetDemonPlayer")
    return None