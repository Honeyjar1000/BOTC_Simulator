from src.StoryTeller.StoryTellerBT import StoryTellerBT
from src.StoryTeller.StoryTellerBB import StoryTellerBB
from src.Characters.EnumCharacter import Characters
from src.Utils.FindPlayer import CheckIfCharacterInPlay, GetAlivePlayersCount
import random

class StoryTeller:

    #######################################################
    #######################################################
    ###
    ###     This Class will be responsible for alot.
    ###
    #######################################################
    #######################################################

    def __init__(self, _players, _scipt, _player_count, _wait_duration=1):

        # Create BB
        self.black_board = StoryTellerBB(players=_players, scipt=_scipt, player_count=_player_count)
        self.BT = StoryTellerBT(story_teller=self, wait_duration=_wait_duration)

        
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
                if (player.character.alignment == 'Good') and (type(player.character) != Characters.RECLUSE):
                    good_players.append(player)
            self.black_board.grimoir.data.data["red_herring"] = random.sample(good_players, 1)[0]

    def check_scarlet_woman_pass(self, executed_player):
        print("WE HERE 1")
        if type(executed_player.character) == Characters.IMP.value:
            print("WE HERE 2")
            alive_player_count = GetAlivePlayersCount(self.black_board.players)
            if alive_player_count >= 5:
                print("WE HERE 3")
                b_sw_in_play, sw_player = CheckIfCharacterInPlay(Characters.SCARLET_WOMAN, self.black_board.players)
                if (b_sw_in_play == True) and (sw_player.alive == True):
                    sw_player.character = Characters.IMP.value()
                    print("WE HERE 4", sw_player.character)
