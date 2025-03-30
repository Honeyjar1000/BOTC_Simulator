from src.Utils.ActionOutputData import ActionOutputData

class Grimoir:

    def __init__(self):
        self.data = ActionOutputData()
    
    def get_spy_data(self, action_output):
        action_output.data["poisoner_hits"] = self.data.data["poisoner_hits"]
        action_output.data["red_herring"] = self.data.data["red_herring"]
        action_output.data["demon_bluffs"] = self.data.data["demon_bluffs"]
        action_output.data["player_roles"] = self.data.data["player_roles"]
        return action_output
        
        
    def assign_player_characters(self, players):
        data_output = {}
        for (i, key) in enumerate(players):
            player = players[key]
            data_output[player.player_name] = player.character
        self.data.data["player_roles"] = data_output
        return data_output