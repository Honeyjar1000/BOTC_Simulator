from src.Utils.ActionOutputData import ActionOutputData

class Grimoir:

    def __init__(self):
        self.data = ActionOutputData()
    
    def get_spy_data(self, action_output):
        action_output.data["poisoner_hits"] = self.data.data["poisoner_hits"]
        action_output.data["red_herring"] = self.data.data["red_herring"]
        action_output.data["demon_bluffs"] = self.data.data["demon_bluffs"]
        action_output.data["player_roles"] = self.data.data["player_roles"]
        action_output.data["butler_picks"] = self.data.data["butler_picks"]
        action_output.data["washer_woman_info_correct"] = self.data.data["washer_woman_info_correct"]
        action_output.data["washer_woman_info_wrong"] = self.data.data["washer_woman_info_wrong"]
        action_output.data["librarian_info_correct"] = self.data.data["librarian_info_correct"]
        action_output.data["librarian_info_wrong"] = self.data.data["librarian_info_wrong"]
        action_output.data["investigator_info_correct"] = self.data.data["investigator_info_correct"]
        action_output.data["investigator_info_wrong"] = self.data.data["investigator_info_wrong"]
        action_output.data["monk_protects"] = self.data.data["monk_protects"]
        action_output.data["demon_picks"] = self.data.data["demon_picks"]

        return action_output
        
        
    def assign_player_characters(self, players):
        data_output = {}
        for (i, key) in enumerate(players):
            player = players[key]
            data_output[player.player_name] = player.character
        self.data.data["player_roles"] = data_output
        return data_output