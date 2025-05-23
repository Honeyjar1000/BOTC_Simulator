from src.Characters.Minion.Minion import Minion
from src.Actions.Action import Action
from src.Player.Player import Player

class C_Baron(Minion):
    
    def __init__(self):
        super().__init__(character_name='Baron')

    def TakeNightAction(self, action:Action, player:Player):
        return super().TakeNightAction(action, player)