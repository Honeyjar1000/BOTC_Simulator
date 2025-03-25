from src.StoryTeller.StoryTellerBT import StoryTellerBT
from src.StoryTeller.StoryTellerBB import StoryTellerBB

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
        self.BB = StoryTellerBB(players=_players, scipt=_scipt, player_count=_player_count)
        self.BT = StoryTellerBT(story_teller=self)

        
    def tick(self):
        action = self.BT.tick()
        
        return action
