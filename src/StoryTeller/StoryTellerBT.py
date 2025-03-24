import py_trees
import time


from src.StoryTeller.BTNodes.NodeST_MinionFirstNightInfo import NodeST_MinionFirstNightInfo
from src.StoryTeller.BTNodes.NodeST_DemonFirstNightInfo import NodeST_DemonFirstNightInfo
from src.StoryTeller.BTNodes.NodeST_ConditionFirstNight import NodeST_ConditionFirstNight
from src.StoryTeller.BTNodes.NodeST_EndFirstNight import NodeST_EndFirstNight
from src.StoryTeller.BTNodes.NodeST_ConditionOtherNight import NodeST_ConditionOtherNight
from src.StoryTeller.BTNodes.NodeST_EndOtherNight import  NodeST_EndOtherNight
from src.StoryTeller.BTNodes.NodeST_ConditionDay import NodeST_ConditionDay
from src.StoryTeller.BTNodes.NodeST_CallTownSquare import NodeST_CallTownSquare
from src.StoryTeller.BTNodes.NodeST_ConditionTownSquare import NodeST_ConditionTownSquare
from src.StoryTeller.BTNodes.NodeST_EndDay import NodeST_EndDay

class  StoryTellerBT():

    def __init__(self, story_teller):
        
        self.story_teller = story_teller

        # Create BT
        self.root = py_trees.composites.Selector(name="Root", memory=False)

        # Main Phases
        node_first_nighttime = py_trees.composites.Sequence(name="Root", memory=True)
        node_nighttime = py_trees.composites.Sequence(name="Root", memory=True)
        node_daytime = py_trees.composites.Sequence(name="Root", memory=True)
        node_townsquare = py_trees.composites.Sequence(name="Root", memory=True)
        
        self.root.add_children([node_first_nighttime, node_nighttime, node_daytime, node_townsquare])

        #############################
        # First Night
        #############################
        node_condition_first_night = NodeST_ConditionFirstNight("Check First Night Condition", black_board=self.story_teller.BB)
        node_first_night_minion_info = NodeST_MinionFirstNightInfo("First Night Minion Info", black_board=self.story_teller.BB)
        node_first_night_demon_info = NodeST_DemonFirstNightInfo("First Night Demon Info", black_board=self.story_teller.BB)

        # Other info

        node_end_first_night = NodeST_EndFirstNight("End First Night", black_board=self.story_teller.BB)
        
        node_first_nighttime.add_children([node_condition_first_night, node_first_night_demon_info, node_first_night_minion_info, node_end_first_night])

        #############################
        # Other Night
        #############################
        node_condition_other_night = NodeST_ConditionOtherNight("Check Other Night Condition", black_board=self.story_teller.BB)
        node_end_other_night = NodeST_EndOtherNight("End Other Night", black_board=self.story_teller.BB)
        node_nighttime.add_children([node_condition_other_night, node_end_other_night])

        #############################
        # Day Time
        #############################
        node_condition_day = NodeST_ConditionDay("Check Day Condition", black_board=self.story_teller.BB)
        node_call_townsquare = NodeST_CallTownSquare("Call Townsquare", black_board=self.story_teller.BB)
        node_daytime.add_children([node_condition_day, node_call_townsquare])

        #############################
        # Town Square
        #############################
        node_condition_day = NodeST_ConditionTownSquare("Check TownSquare Condition", black_board=self.story_teller.BB)
        node_call_townsquare = NodeST_EndDay("End Day", black_board=self.story_teller.BB)
        node_townsquare.add_children([node_condition_day, node_call_townsquare])


    def tick(self):
        action = self.root.tick_once()
        return action
    

if __name__ == "__main__":
    bt = StoryTellerBT()
    bt.tick()