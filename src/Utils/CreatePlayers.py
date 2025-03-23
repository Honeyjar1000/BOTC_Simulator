

def CreatePlayers(character_list, player_dict):
    from src.Characters import Character
    from src.Player.Player import Player
    from typing import List
    for (i, key) in enumerate(player_dict):
        character = character_list[i]
        new_player = Player(character=character, name=key)
        player_dict[key] = new_player

    return player_dict

def CheckIfCharacterInPlay(character, player_dict):
    from src.Characters import Character
    from src.Player.Player import Player
    from typing import List
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