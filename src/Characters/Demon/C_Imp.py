from src.Characters.Demon.Demon import Demon
from src.Actions.Action import Action
from src.Player.PlayerBrain import Brain

class C_Imp(Demon):
    def __init__(self):
        super().__init__(character_name='Imp')
    
    def TakeNightAction(self, action:Action, player_brain:Brain):
        return super().TakeNightAction(action, player_brain)