import random

def GetBaseCharacterTypeDistribution(player_count):
    match player_count:
        case 5: return [3, 0, 1]
        case 6: return [3, 1, 1]
        case 7: return [5, 0, 1]
        case 8: return [5, 1, 1]
        case 9: return [5, 2, 1]
        case 10: return [7, 0, 2]
        case 11: return [7, 1, 2]
        case 12: return [7, 2, 2]
        case 13: return [9, 0, 3]
        case 14: return [9, 1, 3]
        case 15: return [9, 2, 3]


def GetRandomCharactersAndBluffsTB(character_type_dist):

    from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman
    from src.Characters.TownsFolk.C_Librarian import C_Librarian
    from src.Characters.TownsFolk.C_Investigator import C_Investigator
    from src.Characters.TownsFolk.C_Chef import C_Chef
    from src.Characters.TownsFolk.C_Empath import C_Empath
    from src.Characters.TownsFolk.C_FortuneTeller import C_FortuneTeller
    from src.Characters.TownsFolk.C_Undertaker import C_Undertaker
    from src.Characters.TownsFolk.C_Monk import C_Monk
    from src.Characters.TownsFolk.C_RavenKeeper import C_RavenKeeper
    from src.Characters.TownsFolk.C_Virgin import C_Virgin
    from src.Characters.TownsFolk.C_Slayer import C_Slayer
    from src.Characters.TownsFolk.C_Soldier import C_Soldier
    from src.Characters.TownsFolk.C_Mayor import C_Mayor
    from src.Characters.Outsider.C_Butler import C_Butler
    from src.Characters.Outsider.C_Saint import C_Saint
    from src.Characters.Outsider.C_Recluse import C_Recluse
    from src.Characters.Outsider.C_Drunk import C_Drunk
    from src.Characters.Minion.C_Poisoner import C_Poisoner
    from src.Characters.Minion.C_Spy import C_Spy
    from src.Characters.Minion.C_Baron import C_Baron
    from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
    from src.Characters.Demon.C_Imp import C_Imp

    # Always add Imp
    characters = [C_Imp]

    # First Choose Minions
    minions = [C_Poisoner, C_Spy, C_Baron, C_ScarletWoman]
    characters += random.sample(minions, character_type_dist[2])
    
    # Edit Character Distribution If Baron In Play
    if C_Baron in characters:
        character_type_dist[0] -= 2
        character_type_dist[1] += 2

    # Next Choose Outsiders
    outsiders = [C_Butler, C_Saint, C_Recluse, C_Drunk]
    characters += random.sample(outsiders, character_type_dist[1])
    
    # Finally Choose townsfolk
    townsfolk = [C_WasherWoman, C_Librarian, C_Investigator, C_Chef, C_Empath, C_FortuneTeller, C_Undertaker,
                 C_Monk, C_RavenKeeper, C_Virgin, C_Slayer, C_Soldier, C_Mayor]
    characters += random.sample(townsfolk, character_type_dist[0])
    
    # Create instances of the characters
    character_instances = []
    for character in characters:
        current_character = character()  # Create an instance of the character
        character_instances.append(current_character)

    # Create a list of remaining characters that are not in the character_instances list
    all_characters = [C_Butler, C_Saint, C_Recluse, C_Drunk, 
                      C_WasherWoman, C_Librarian, C_Investigator, C_Chef, C_Empath, C_FortuneTeller, 
                      C_Undertaker, C_Monk, C_RavenKeeper, C_Virgin, C_Slayer, C_Soldier, C_Mayor]
    
    # Remove the characters already in character_instances
    remaining_characters = [char for char in all_characters if char not in characters]
    
    # Select 3 random characters from the remaining ones
    additional_characters = random.sample(remaining_characters, 3)
    
    # Create instances of the additional characters
    demon_bluffs = []
    for character in additional_characters:
        current_character = character()
        demon_bluffs.append(current_character)

    # Shuffle the final list of character instances
    random.shuffle(character_instances)
    
    return character_instances, demon_bluffs

def GetCharacterNightOrder(script):
    
    from src.Characters.TownsFolk.C_WasherWoman import C_WasherWoman
    from src.Characters.TownsFolk.C_Librarian import C_Librarian
    from src.Characters.TownsFolk.C_Investigator import C_Investigator
    from src.Characters.TownsFolk.C_Chef import C_Chef
    from src.Characters.TownsFolk.C_Empath import C_Empath
    from src.Characters.TownsFolk.C_FortuneTeller import C_FortuneTeller
    from src.Characters.TownsFolk.C_Undertaker import C_Undertaker
    from src.Characters.TownsFolk.C_Monk import C_Monk
    from src.Characters.TownsFolk.C_RavenKeeper import C_RavenKeeper
    from src.Characters.TownsFolk.C_Virgin import C_Virgin
    from src.Characters.TownsFolk.C_Slayer import C_Slayer
    from src.Characters.TownsFolk.C_Soldier import C_Soldier
    from src.Characters.TownsFolk.C_Mayor import C_Mayor
    from src.Characters.Outsider.C_Butler import C_Butler
    from src.Characters.Outsider.C_Saint import C_Saint
    from src.Characters.Outsider.C_Recluse import C_Recluse
    from src.Characters.Outsider.C_Drunk import C_Drunk
    from src.Characters.Minion.C_Poisoner import C_Poisoner
    from src.Characters.Minion.C_Spy import C_Spy
    from src.Characters.Minion.C_Baron import C_Baron
    from src.Characters.Minion.C_ScarletWoman import C_ScarletWoman
    from src.Characters.Demon.C_Imp import C_Imp
    
    first_night_order, other_night_order = [], []
    if script == "TB":
        first_night_order = [C_Poisoner, C_Spy, C_WasherWoman, C_Librarian, C_Investigator, C_Chef, C_Empath, C_FortuneTeller, C_Butler]
        other_night_order = [C_Poisoner, C_Monk, C_Spy, C_ScarletWoman, C_Imp, C_RavenKeeper, C_Undertaker, C_Empath, C_FortuneTeller, C_Butler]
    return first_night_order, other_night_order