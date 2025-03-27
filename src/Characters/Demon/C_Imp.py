from src.Characters.Demon.Demon import Demon
from src.Actions.Action import Action
from src.Player.Player import Player

class C_Imp(Demon):
    def __init__(self):
        super().__init__(character_name='Imp')
    
    def TakeNightAction(self, action:Action, player:Player):
        return super().TakeNightAction(action, player)