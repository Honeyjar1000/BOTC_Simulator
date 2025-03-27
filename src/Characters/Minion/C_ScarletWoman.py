from src.Characters.Minion.Minion import Minion
from src.Actions.Action import Action
from src.Player.PlayerBrain import Brain

class C_ScarletWoman(Minion):
    
    def __init__(self):
        super().__init__(character_name='ScarletWoman')

    def TakeNightAction(self, action:Action, player_brain:Brain):
        return super().TakeNightAction(action, player_brain)