from src.Utils.ActionOutputData import *

class BlackBoard:
    def __init__(self, name, character):

        self.data = {
            "player_name": name,
            "player_character": character,
            "demon_player": None,
            "minion_players": None,
            "demon_bluffs": None,
            "washer_woman_info": None,
            "librarian_info": None
        }

        self.data_desc = {
            "player_name": 'Their name is',
            "player_character": 'Their character is',
            "demon_player": 'The demon is',
            "minion_players": 'The minions are',
            "demon_bluffs": 'The demon bluffs are ',
            "washer_woman_info": 'WasherWoman info: ',
            "librarian_info": "Librarian info"
        }

    def update(self, ActionOutputs:ActionOutputData):
        for (i, key) in enumerate(ActionOutputs.data):
            if ActionOutputs.data[key] is not None:
                self.data[key] = ActionOutputs.data[key]

    def print_beliefs(self):
        s = f'{self.data['player_name']} believes:\n'
        for (i, key) in enumerate(self.data):
            if (key is not 'player_name') and (self.data[key] is not None):
                s += f'    - {self.data_desc[key]} {str(self.data[key])}\n'
        print(s)