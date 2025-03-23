
from src.Characters.Character import Character
from src.Actions.Action import Action


class Minion(Character):

    def __init__(self, character_name):
        super().__init__(character_name=character_name, character_type='Minion', alignment='Evil')

    def TakeNightAction(self, action:Action):
        output = action.TakeAction()
        return output