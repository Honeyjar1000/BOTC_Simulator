from src.Actions.Action import Action
from src.Utils.ActionOutputData import ActionOutputData
from src.Characters.EnumCharacter import Characters
from src.Utils.FindPlayer import CheckIfCharacterInPlay

class A_ImpMove(Action):
    
    def __init__(self, players):
        self.players = players
        return

    def __str__(self):
        return "[Imp Moves]"

    def TakeAction(self, story_teller, player):

        picked_player = player.brain.think_pick_player()
        action_output = ActionOutputData()

        # Monk
        b_monk_in_play, monk_player = CheckIfCharacterInPlay(Characters.MONK, story_teller.black_board.players)
        if b_monk_in_play:
            if (monk_player.alive == True) and (picked_player.b_is_monk_protected):
                print(f'Imp picks {picked_player} who monk protected, no kill.')
                return action_output

        # Mayor

        # Solider
        if (type(picked_player.character)==Characters.SOLDIER) and (picked_player.b_is_poisoned == False):
            print(f'Imp picks {picked_player} who is the soldier, no kill.')
            return action_output
        
        # Add star pass
        
        action_output.data["demon_picks"] = picked_player
        story_teller.black_board.grimoir.data.data["demon_picks"] = picked_player     # Repeat for everything that would have a reminder token
        picked_player.alive = False
        print("Imp kills", str(picked_player))
        return action_output