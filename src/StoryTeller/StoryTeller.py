from src.StoryTeller.StoryTellerBT import StoryTellerBT
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Characters.EnumCharacter import Characters
from src.Utils.FindPlayer import CheckIfCharacterInPlay
import random

class StoryTeller:

    #######################################################
    #######################################################
    ###
    ###     This Class will be responsible for alot.
    ###
    #######################################################
    #######################################################

    def __init__(self, _players, _scipt, _player_count):

        # Create BB
        self.black_board = StoryTellerBB(players=_players, scipt=_scipt, player_count=_player_count)
        self.BT = StoryTellerBT(story_teller=self)

        
    def tick(self):
        action = self.BT.tick()
        
        return action

    def PickRedHerring(self):
        b_in_play, _ = CheckIfCharacterInPlay(Characters.FORTUNE_TELLER, self.black_board.players)
        if b_in_play:
            # Get the list of other players
            player_list = list(self.black_board.players.values())
            # Filter players who have a good alignment and are not the imp

            good_players = []
            for player in player_list:
                if (player.character.alignment == 'Good'):
                    good_players.append(player)
            self.black_board.red_herring = random.choice(good_players)
