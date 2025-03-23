from src.Characters import Character
from src.Actions import Action
from src.Player.BlackBoard import BlackBoard

class Player():

    def __init__(self, character:Character, name:str):
        self.character = character
        self.player_name = name
        self.bb = BlackBoard(name, character.GetPercievedCharacter())

    def WakeAtNight(self, action:Action):
        print(f'{self.player_name} takes action {str(action)}')
        action_output = self.character.TakeNightAction(action)
        self.bb.update(action_output)

    def __str__(self):
        return self.player_name
    
    def __repr__(self):
        return self.player_name