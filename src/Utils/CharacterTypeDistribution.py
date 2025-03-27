import random
from src.Characters.EnumCharacter import Characters

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



def GetAllOutsiderRoles():
    return [Characters.BUTLER, Characters.DRUNK, Characters.SAINT, Characters.RECLUSE]

def GetRandomCharactersAndBluffsTB(character_type_dist):
  
    # Always add Imp
    characters = [Characters.IMP]

    # First Choose Minions
    minions = [Characters.POISONER, Characters.SPY, Characters.BARON, Characters.SCARLET_WOMAN]
    characters += random.sample(minions, character_type_dist[2])
    
    # Edit Character Distribution If Baron In Play
    if Characters.BARON in characters:
        character_type_dist[0] -= 2
        character_type_dist[1] += 2

    # Next Choose Outsiders
    outsiders = [Characters.BUTLER, Characters.SAINT, Characters.RECLUSE, Characters.DRUNK]
    characters += random.sample(outsiders, character_type_dist[1])
    
    # Finally Choose townsfolk
    townsfolk = [Characters.WASHER_WOMAN, Characters.LIBRARIAN, Characters.INVESTIGATOR, Characters.CHEF, 
                 Characters.EMPATH, Characters.FORTUNE_TELLER, Characters.UNDERTAKER, Characters.MONK, 
                 Characters.RAVEN_KEEPER, Characters.VIRGIN, Characters.SLAYER, Characters.SOLDIER, Characters.MAYOR]
    characters += random.sample(townsfolk, character_type_dist[0])
    
    # Create instances of the characters
    character_instances = []
    for character in characters:
        current_character = character.value()  # Create an instance of the character
        character_instances.append(current_character)


    ### Demon Bluffs...
    # Create a list of remaining characters that are not in the character_instances list
    all_characters = [  Characters.BUTLER, Characters.SAINT, Characters.RECLUSE, Characters.DRUNK, 
                        Characters.WASHER_WOMAN, Characters.LIBRARIAN, Characters.INVESTIGATOR, Characters.CHEF, 
                        Characters.EMPATH, Characters.FORTUNE_TELLER, Characters.UNDERTAKER, Characters.MONK, 
                        Characters.RAVEN_KEEPER, Characters.VIRGIN, Characters.SLAYER, Characters.SOLDIER, Characters.MAYOR]
    
    # Remove the characters already in character_instances
    remaining_characters = [char for char in all_characters if char not in characters]
    
    # Select 3 random characters from the remaining ones
    additional_characters = random.sample(remaining_characters, 3)
    
    # Create instances of the additional characters
    demon_bluffs = []
    for character in additional_characters:
        current_character = character.value()
        demon_bluffs.append(current_character)

    # Shuffle the final list of character instances
    random.shuffle(character_instances)
    
    return character_instances, demon_bluffs

def GetCharacterNightOrder(script):

    first_night_order, other_night_order = [], []
    if script == "TB":
        first_night_order = [   Characters.POISONER, Characters.SPY, Characters.WASHER_WOMAN, Characters.LIBRARIAN, 
                                Characters.INVESTIGATOR, Characters.CHEF, Characters.EMPATH, Characters.FORTUNE_TELLER, Characters.BUTLER]
        other_night_order = [   Characters.POISONER, Characters.MONK, Characters.SPY, Characters.SCARLET_WOMAN, 
                                Characters.IMP, Characters.RAVEN_KEEPER, Characters.UNDERTAKER, Characters.EMPATH,
                                Characters.FORTUNE_TELLER, Characters.BUTLER]
    return first_night_order, other_night_order
