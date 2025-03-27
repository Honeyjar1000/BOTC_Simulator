from src.Utils.ActionOutputData import *

class BlackBoard:
    def __init__(self, name, character, player_dict):

        self.data = {
            "player_name": name,
            "player_character": character,
            "other_players": player_dict,
            "demon_player": None,
            "minion_players": None,
            "demon_bluffs": None,
            "poisoner_hits": None,
            "washer_woman_info": None,
            "librarian_info": None,
            "investigator_info":None,
            "chef_info":None
        }

        self.data_desc = {
            "player_name": 'Their name is',
            "player_character": 'Their character is',
            "other_players": " Other players are ",
            "demon_player": 'The demon is',
            "minion_players": 'The minions are',
            "poisoner_hits": "Poisoner hits",
            "demon_bluffs": 'The demon bluffs are ',
            "washer_woman_info": 'WasherWoman info is',
            "librarian_info": "Librarian info is",
            "investigator_info": "Investigator info is",
            "chef_info": "Chef info is"
        }

    def update(self, ActionOutputs:ActionOutputData):
        for (i, key) in enumerate(ActionOutputs.data):
            if ActionOutputs.data[key] is not None:
                self.data[key] = ActionOutputs.data[key]

    def print_beliefs(self):
        s = f'{self.data['player_name']} believes:\n'
        for (i, key) in enumerate(self.data):
            if (key is not 'player_name') and (key is not 'other_players') and (self.data[key] is not None):
                s += f'    - {self.data_desc[key]} {str(self.data[key])}\n'
        print(s)