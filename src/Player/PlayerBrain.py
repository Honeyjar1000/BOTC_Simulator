import random

class Brain:
    def __init__(self, black_board):
        self.black_board=black_board

    def think(self):
        return random.random()
    
    def think_pick_player(self):
        # for now always pick random player
        player_list = list(self.black_board.data['other_players'].values())
        random_player = random.sample(player_list, 1)[0]
        return random_player
    
    def think_pick_2_players(self):
        # Get the list of other players
        player_list = list(self.black_board.data['other_players'].values())
        
        # Pick two unique random players
        random_players = random.sample(player_list, 2)
        return random_players
    
    def think_pick_player_not_self(self, self_player):
        # Get the list of other players
        player_list = list(self.black_board.data['other_players'].values())

        # Filter out the player that is 'self'
        other_players = [player for player in player_list if player != self_player]

        # Pick a random player who is not self
        return random.choice(other_players)