from src.Player.BlackBoard import BlackBoard
from src.Player.PlayerBrain import Brain

class Player():

    def __init__(self, character, name:str, all_players:dict):
        self.character = character
        self.player_name = name
        self.bb = BlackBoard(name, character.GetPercievedCharacter(), all_players)
        self.brain = Brain(black_board=self.bb)
        self.alive = True
        self.b_is_poisoned = False


    def WakeAtNight(self, story_teller, action):
        print(f'{self.player_name} takes action {str(action)}')
        action_output = action.TakeAction(story_teller=story_teller, player=self)
        self.bb.update(action_output)

    def __str__(self):
        return self.player_name
    
    def __repr__(self):
        return self.player_name