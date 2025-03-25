from src.Characters.Minion.C_Poisoner import C_Poisoner
from src.Characters.Minion.C_Baron import C_Baron
from src.Characters.Minion.C_Spy import C_Spy
from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
from src.Characters.Demon.C_Imp import C_Imp
from src.Utils.CharacterTypeDistribution import GetAllTownsfolkRolls
import random

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

def FindWashWomanPings(players):
    ##########################################################
    ##########################################################
    ###
    ###     Return washer woman info
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - [[Class], [Person 1, Person 2]]
    ###     Where either Person 1 or Person 2 is character Class
    ###
    ##########################################################
    ##########################################################
    
    townsfolk_characters = GetAllTownsfolkRolls()
    b_character_in_play = False
    while not b_character_in_play:
        random_character = random.sample(townsfolk_characters, 1)[0]
        b_in_play, player_townsfolk = CheckIfCharacterInPlay(random_character, players)
        if b_in_play:
            b_character_in_play = True

    final_player_output = [player_townsfolk]
    b_found_false_ping = False
    while not b_found_false_ping:
        random_player = random.sample(list(players.items()), 1)[0][1]
        print("ln 103: ", random_player.bb.data["player_name"], player_townsfolk.bb.data["player_name"])
        if random_player.bb.data["player_name"] != player_townsfolk.bb.data["player_name"]:
            final_player_output.append(random_player)
            b_found_false_ping = True
    
    random.shuffle(final_player_output)

    final_output = [random_character, final_player_output]

    return final_output
