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
            "spy_info":None,
            "washer_woman_info": None,
            "librarian_info": None,
            "investigator_info":None,
            "chef_info":None,
            "empath_info":None,
            "fortune_teller_info":None,
            "butler_picks": None,
            "red_herring":None,
            "washer_woman_info_correct":None,
            "washer_woman_info_wrong":None,            
            "librarian_info_correct":None,
            "librarian_info_wrong":None,
            "investigator_info_correct":None,
            "investigator_info_wrong":None,
            "monk_protects":None,
            "demon_picks":None,
            "player_roles": []
        }

        self.data_desc = {
            "player_name": 'Their name is',
            "player_character": 'Their character is',
            "other_players": " Other players are ",
            "demon_player": 'The demon is',
            "minion_players": 'The minions are',
            "poisoner_hits": "Poisoner hits",
            "spy_info": "Spy info",
            "demon_bluffs": 'The demon bluffs are ',
            "washer_woman_info": 'WasherWoman info is',
            "librarian_info": "Librarian info is",
            "investigator_info": "Investigator info is",
            "chef_info": "Chef info is",
            "empath_info":"Empath info is",
            "fortune_teller_info":"Fortune Teller info is",
            "butler_picks": "Butler picks",
            "red_herring":"Red herring is",
            "washer_woman_info_correct":"Correct washer woman info is ",
            "washer_woman_info_wrong":"Wrong washer woman info is ",            
            "librarian_info_correct":"Correct librarian info is ",
            "librarian_info_wrong":"Wrong librarian info is ",
            "investigator_info_correct":"Correct investigator info is ",
            "investigator_info_wrong":"Wrong investigator info is ",
            "monk_protects":"Monk is protecting",
            "demon_picks":"Demon picks",
            "player_roles": "Roles of other players are "
        }

    def update(self, ActionOutputs:ActionOutputData):
        for (i, key) in enumerate(ActionOutputs.data):
            if ActionOutputs.data[key] is not None:
                self.data[key] = ActionOutputs.data[key]

    def print_beliefs(self):
        s = f'{self.data['player_name']} believes:\n'
        for (i, key) in enumerate(self.data):
            if (key is not 'player_name') and (key is not 'player_roles') and (key is not 'other_players') and (self.data[key] is not None):
                s += f'    - {self.data_desc[key]} {str(self.data[key])}\n'
            if (key is 'player_roles'):
                for (i, key2) in enumerate(self.data[key]):
                    character = self.data[key][key2]
                    s += f'    - {key2} is {str(character)}\n'
        print(s)