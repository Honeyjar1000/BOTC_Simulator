from src.Characters.Minion.Minion import Minion
from src.Actions.Action import Action


class C_ScarletWoman(Minion):
    
    def __init__(self):
        super().__init__(character_name='ScarletWoman')

    def TakeNightAction(self, action:Action):
        return super().TakeNightAction(action)