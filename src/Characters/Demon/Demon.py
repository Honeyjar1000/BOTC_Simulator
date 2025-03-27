from src.Characters import Character
from src.Actions.Action import Action
from src.Player.PlayerBrain import Brain

class Demon(Character):

    def __init__(self, character_name):
        super().__init__(character_name=character_name, character_type='Demon', alignment='Evil')

    def TakeNightAction(self, action:Action, player_brain:Brain):
        output = action.TakeAction()
        return output