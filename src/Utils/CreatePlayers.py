from src.Player.Player import Player

def CreatePlayers(character_list, player_dict):
    for (i, key) in enumerate(player_dict):
        character = character_list[i]
        new_player = Player(character=character, name=key, all_players=player_dict)
        player_dict[key] = new_player

    return player_dict

