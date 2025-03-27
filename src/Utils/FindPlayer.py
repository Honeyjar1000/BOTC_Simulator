from src.Characters.EnumCharacter import Characters
from src.Utils.CharacterTypeDistribution import GetAllOutsiderRoles
import random
from src.Utils.InfoClasses.FirstNightInfoClass import FirstNightInfoClass

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
    ###     Find Demon Player
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - A Player that is the demon
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

    townsfolk_and_spy_characters = [Characters.LIBRARIAN, Characters.INVESTIGATOR, Characters.CHEF, 
            Characters.EMPATH, Characters.FORTUNE_TELLER, 
            Characters.UNDERTAKER, Characters.MONK, Characters.RAVEN_KEEPER, 
            Characters.VIRGIN, Characters.SLAYER, Characters.SOLDIER, Characters.MAYOR, Characters.SPY]
    
    townsfolks = [Characters.LIBRARIAN, Characters.INVESTIGATOR, Characters.CHEF, 
            Characters.EMPATH, Characters.FORTUNE_TELLER, 
            Characters.UNDERTAKER, Characters.MONK, Characters.RAVEN_KEEPER, 
            Characters.VIRGIN, Characters.SLAYER, Characters.SOLDIER, Characters.MAYOR]


    b_character_in_play = False
    while not b_character_in_play:
        random_character = random.sample(townsfolk_and_spy_characters, 1)[0]
        b_in_play, player_townsfolk = CheckIfCharacterInPlay(random_character, players)
        if b_in_play:
            b_character_in_play = True

    final_player_output = [player_townsfolk]
    b_found_false_ping = False
    while not b_found_false_ping:
        if random_character == Characters.SPY:
            random_character = random.sample(townsfolks, 1)[0]

        random_player = random.sample(list(players.items()), 1)[0][1]
        b_in_play, player_washer_woman = CheckIfCharacterInPlay(Characters.WASHER_WOMAN, players)
        if (random_player.bb.data["player_name"] != player_townsfolk.bb.data["player_name"]) and (random_player.bb.data["player_name"] != player_washer_woman.bb.data["player_name"]):
            final_player_output.append(random_player)
            b_found_false_ping = True
    
    random.shuffle(final_player_output)
    final_output = [random_character, final_player_output]
    result = FirstNightInfoClass(data=final_output)
    return result

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
    result = FirstNightInfoClass(data=final_output)
    return result

def FindInvestigatorPings(players):
    
    ##########################################################
    ##########################################################
    ###
    ###     Return Investigator info
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - [[Class], [Person 1, Person 2]]
    ###     Where either Person 1 or Person 2 is a particular
    ###     Minion
    ###
    ##########################################################
    ##########################################################
    
    possible_pings = [  Characters.BARON, Characters.SPY, 
                        Characters.SCARLET_WOMAN, Characters.POISONER,
                        Characters.RECLUSE]
    random.shuffle(possible_pings)
    b_character_in_play = False
    i = 0
    while (i < len(possible_pings)) and (b_character_in_play == False):
        random_minion = possible_pings[i]
        b_in_play, player_minion = CheckIfCharacterInPlay(random_minion, players)
        if b_in_play:
            b_character_in_play = True
        i += 1
    
    if b_character_in_play:
        if random_minion == Characters.RECLUSE:
            random_minion = random.sample([Characters.SPY, Characters.BARON, Characters.POISONER, Characters.SCARLET_WOMAN], 1)[0]
        final_player_output = [player_minion]
        b_found_false_ping = False
        while not b_found_false_ping:
            random_player = random.sample(list(players.items()), 1)[0][1]
            b_in_play, player_investigator = CheckIfCharacterInPlay(Characters.INVESTIGATOR, players)
            if (random_player.bb.data["player_name"] != player_minion.bb.data["player_name"]) and (random_player.bb.data["player_name"] != player_investigator.bb.data["player_name"]):
                final_player_output.append(random_player)
                b_found_false_ping = True
        random.shuffle(final_player_output)
        final_output = [random_minion, final_player_output]
    else:
        final_output = 0
    result = FirstNightInfoClass(data=final_output)
    return result

def GetChefNumber(players):
    
    ##########################################################
    ##########################################################
    ###
    ###     Return Chef Info
    ###
    ###     Inputs
    ###         - player_dict : dictionary of all players
    ###     Outputs
    ###         - int
    ###     How many pairs of evil players
    ###     For now, make the change to ping spy as evil 50%
    ###     and chance to ping recluse as evil as 50%
    ###
    ##########################################################
    ##########################################################
    
    pair_count = 0
    last_was_evil = False

    # Convert players to a list for easy index-based access
    player_list = list(players.values())
    
    # Loop through players and compare adjacent players
    for i in range(len(player_list)):
        player = player_list[i]
        player_character = player.character
        b_player_is_evil = False

        if type(player_character) == Characters.RECLUSE.value:
            if random.random() > 0.4:
                b_player_is_evil = True
        elif type(player_character) == Characters.SPY.value:
            if random.random() > 0.6:
                b_player_is_evil = True
        elif type(player_character) in [Characters.IMP.value, Characters.BARON.value, Characters.SCARLET_WOMAN.value, Characters.POISONER.value]:
            b_player_is_evil = True
        
        # Check adjacent players
        if last_was_evil and b_player_is_evil:
            pair_count += 1
        last_was_evil = b_player_is_evil

    # Compare the first player with the last player to account for the circle
    first_player = player_list[0]
    last_player = player_list[-1]
    first_player_is_evil = False

    if type(first_player.character) == Characters.RECLUSE.value:
        if random.random() > 0.4:
            first_player_is_evil = True
    elif type(first_player.character) == Characters.SPY.value:
        if random.random() > 0.6:
            first_player_is_evil = True
    elif type(first_player.character) in [Characters.IMP.value, Characters.BARON.value, Characters.SCARLET_WOMAN.value, Characters.POISONER.value]:
        first_player_is_evil = True

    if last_was_evil and first_player_is_evil:
        pair_count += 1

    return pair_count

def GetNeighbours(players, player):
    # Convert dictionary values to a list for indexing
    player_list = list(players.values())

    # Find the index of the given player
    player_index = player_list.index(player)

    # Get neighbors in a circular manner
    left_neighbor = player_list[(player_index - 1) % len(player_list)]
    right_neighbor = player_list[(player_index + 1) % len(player_list)]

    return left_neighbor, right_neighbor

def CheckPlayerAlignment(player):
    if type(player.character) in [Characters.IMP.value, Characters.SCARLET_WOMAN.value, Characters.POISONER.value, Characters.BARON.value]:
        return True
    elif type(player.character) == Characters.SPY.value:
        if random.random() > 0.4:
            return True
    elif type(player.character) == Characters.RECLUSE.value:
        if random.random() > 0.6:
            return True
    return False

def CheckPlayerIsDemonFortuneTeller(player, red_herring):
    if type(player.character) == Characters.IMP.value:
        return True
    elif (player == red_herring):
        return True
    elif type(player.character) == Characters.RECLUSE.value:
        if random.random() > 0.3:
            return True
    return False