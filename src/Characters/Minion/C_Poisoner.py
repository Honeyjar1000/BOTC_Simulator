from src.Characters.Minion.Minion import Minion


class C_Poisoner(Minion):
    
    def __init__(self):
        super().__init__(character_name='Poisoner')

    def TakeNightAction(self, action):
        return super().TakeNightAction(action)