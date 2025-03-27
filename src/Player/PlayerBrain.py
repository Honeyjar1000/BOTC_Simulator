import random

class Brain:
    def __init__(self, black_board):
        self.black_board=black_board

    def think(self):
        return random.random()
    
    def think_pick_player(self):
        player_list = list(self.black_board.data['other_players'].values())
        random_player = random.sample(player_list, 1)[0]
        return random_player