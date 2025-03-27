from src.Characters.Minion.Minion import Minion
from src.Actions.A_PoisonerMove import A_PoisonerMove
from src.Player.Player import Player
from src.Actions.Action import Action

class C_Poisoner(Minion):
    
    def __init__(self):
        super().__init__(character_name='Poisoner')

    # I want to move TakeNightAction to be wholy done by the Player Class
    def TakeNightAction(self, action:Action, player:Player):

        if type(action) == A_PoisonerMove:
             output = action.TakeAction(player)
             print("Poisoner poisons " + str(output.data['poisoner_hits']))
             return output
        else:
            return super().TakeNightAction(action, player)