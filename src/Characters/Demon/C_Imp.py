from src.Characters.Demon.Demon import Demon

class C_Imp(Demon):
    def __init__(self):
        super().__init__(character_name='Imp')
    
    def TakeNightAction(self, action):
        print(action.player_minions)
        return super().TakeNightAction(action)