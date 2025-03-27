from src.Characters.Minion.Minion import Minion
from src.Actions.A_PoisonerMove import A_PoisonerMove
from src.Player.PlayerBrain import Brain
from src.Actions.Action import Action
import random

class C_Poisoner(Minion):
    
    def __init__(self):
        super().__init__(character_name='Poisoner')

    def TakeNightAction(self, action:Action, player_brain:Brain):

        if type(action) == A_PoisonerMove:
             output = action.TakeAction(player_brain)
             print("Poisoner poisons " + str(output.data['poisoner_hits']))
             return output
        else:
            return super().TakeNightAction(action, player_brain)