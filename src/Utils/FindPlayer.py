from src.Characters.EnumCharacter import Characters
from src.Utils.CharacterTypeDistribution import GetAllTownsfolkRolesBesidesWasherWoman, GetAllOutsiderRoles
import random

def CheckIfCharacterInPlay(character, player_dict:dict):

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
        if type(player.character) == character.value:
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
    minions = [Characters.POISONER, Characters.BARON, Characters.SPY, Characters.SCARLET_WOMAN]
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

    b_in_play, player = CheckIfCharacterInPlay(Characters.IMP, players)
    if b_in_play:
        return player
    else:
        print("Error: Can't find demon in Utils.FindPlayer.GetDemonPlayer")
    return None

def FindWashWomanPings(players):

    ##########################################################
    ##########################################################
    ###
    ###     Return librarian info
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - [[Class], [Person 1, Person 2]]
    ###     Where either Person 1 or Person 2 is a particular
    ###     Librarian
    ###     Have to add chance to ping spy as townsfolk
    ###
    ##########################################################
    ##########################################################
    
    townsfolk_characters = GetAllTownsfolkRolesBesidesWasherWoman()
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
        b_in_play, player_washer_woman = CheckIfCharacterInPlay(Characters.WASHER_WOMAN, players)
        if (random_player.bb.data["player_name"] != player_townsfolk.bb.data["player_name"]) and (random_player.bb.data["player_name"] != player_washer_woman.bb.data["player_name"]):
            final_player_output.append(random_player)
            b_found_false_ping = True
    
    random.shuffle(final_player_output)

    final_output = [random_character, final_player_output]

    return final_output


def FindLibrarianPings(players):
    
    ##########################################################
    ##########################################################
    ###
    ###     Return librarian info
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - [[Class], [Person 1, Person 2]]
    ###     Where either Person 1 or Person 2 is a particular
    ###     Outsider
    ###     Have to add chance to ping spy as outsider
    ###
    ##########################################################
    ##########################################################
    
    outsider_characters = GetAllOutsiderRoles()
    random.shuffle(outsider_characters)
    b_character_in_play = False
    i = 0
    while (i < len(outsider_characters)) and (b_character_in_play == False):
        random_outsider = outsider_characters[i]
        b_in_play, player_outsider = CheckIfCharacterInPlay(random_outsider, players)
        if b_in_play:
            b_character_in_play = True
        i += 1
    
    if b_character_in_play:
        final_player_output = [player_outsider]
        b_found_false_ping = False
        while not b_found_false_ping:
            random_player = random.sample(list(players.items()), 1)[0][1]
            b_in_play, player_librarian = CheckIfCharacterInPlay(Characters.LIBRARIAN, players)
            if (random_player.bb.data["player_name"] != player_outsider.bb.data["player_name"]) and (random_player.bb.data["player_name"] != player_librarian.bb.data["player_name"]):
                final_player_output.append(random_player)
                b_found_false_ping = True
        random.shuffle(final_player_output)
        final_output = [random_outsider, final_player_output]
    else:
        final_output = 0
    return final_output
