import py_trees
import time

from src.StoryTeller.BTNodes.NodeST_MinionFirstNightInfo import NodeST_MinionFirstNightInfo
from src.StoryTeller.BTNodes.NodeST_DemonFirstNightInfo import NodeST_DemonFirstNightInfo
from src.StoryTeller.BTNodes.NodeST_ConditionFirstNight import NodeST_ConditionFirstNight
from src.StoryTeller.BTNodes.NodeST_EndFirstNight import NodeST_EndFirstNight
from src.StoryTeller.BTNodes.NodeST_ConditionOtherNight import NodeST_ConditionOtherNight
from src.StoryTeller.BTNodes.NodeST_EndOtherNight import NodeST_EndOtherNight
from src.StoryTeller.BTNodes.NodeST_ConditionDay import NodeST_ConditionDay
from src.StoryTeller.BTNodes.NodeST_CallTownSquare import NodeST_CallTownSquare
from src.StoryTeller.BTNodes.NodeST_ConditionTownSquare import NodeST_ConditionTownSquare
from src.StoryTeller.BTNodes.NodeST_EndDay import NodeST_EndDay
from src.StoryTeller.BTNodes.NodeST_WasherWomanInfo import NodeST_WasherWomanInfo
from src.StoryTeller.BTNodes.NodeST_LibrarianInfo import NodeST_LibrarianInfo
from src.StoryTeller.BTNodes.NodeST_InvestigatorInfo import NodeST_InvestigatorInfo
from src.StoryTeller.BTNodes.NodeST_ChefInfo import NodeST_ChefInfo
from src.StoryTeller.BTNodes.NodeST_PoisonerMove import NodeST_PoisonerMove
from src.StoryTeller.BTNodes.NodeST_EmpathMove import NodeST_EmpathMove
from src.StoryTeller.BTNodes.NodeST_Wait import NodeST_Wait


class StoryTellerBT:
    def __init__(self, story_teller):
        self.story_teller = story_teller
        self.wait_duration = 1
        # Create BT Root
        self.root = py_trees.composites.Selector(name="Root", memory=True)

        # Main Phases
        node_first_nighttime = py_trees.composites.Sequence(name="First Night", memory=True)
        node_nighttime = py_trees.composites.Sequence(name="Other Nights", memory=True)
        node_daytime = py_trees.composites.Sequence(name="Daytime", memory=True)
        node_townsquare = py_trees.composites.Sequence(name="Town Square", memory=True)

        self.root.add_children([node_first_nighttime, node_nighttime, node_daytime, node_townsquare])

        #############################
        # First Night
        #############################
        node_condition_first_night = NodeST_ConditionFirstNight("Check First Night Condition", story_teller=self.story_teller)
        node_wait_1 = NodeST_Wait("Wait", duration=self.wait_duration)
        
        # Minion Info
        node_first_night_minion_info = NodeST_MinionFirstNightInfo("First Night Minion Info", story_teller=self.story_teller)
        node_wait_2 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Demon Info
        node_first_night_demon_info = NodeST_DemonFirstNightInfo("First Night Demon Info", story_teller=self.story_teller)
        node_wait_3 = NodeST_Wait("Wait", duration=self.wait_duration)
        
        # Poisoner
        node_poisoner_moves = NodeST_PoisonerMove("Poisoner Moves", story_teller=self.story_teller)
        node_wait_4 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Spy

        # Washer Woman
        node_do_washer_woman_info = NodeST_WasherWomanInfo("First Night Washer Woman Info", story_teller=self.story_teller)
        node_wait_5 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Librarian
        node_do_librarian_info = NodeST_LibrarianInfo("First Night Librarian Info", story_teller=self.story_teller)
        node_wait_6 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Investigator
        node_do_investigator_info = NodeST_InvestigatorInfo("First Night Investigator Info", story_teller=self.story_teller)
        node_wait_7 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Chef
        node_do_chef_info = NodeST_ChefInfo("First Night Chef Info", story_teller=self.story_teller)
        node_wait_8 = NodeST_Wait("Wait", duration=self.wait_duration)
        
        # Empath
        node_empath_moves = NodeST_EmpathMove("Empath Moves", story_teller=self.story_teller)
        node_wait_9 = NodeST_Wait("Wait", duration=self.wait_duration)

        node_end_first_night = NodeST_EndFirstNight("End First Night", story_teller=self.story_teller)
        node_wait_10 = NodeST_Wait("Wait", duration=self.wait_duration)

        node_first_nighttime.add_children([
            node_condition_first_night, 
            node_wait_1,
            node_first_night_minion_info,
            node_wait_2, 
            node_first_night_demon_info, 
            node_wait_3,
            node_poisoner_moves,
            node_wait_4,
            node_do_washer_woman_info,
            node_wait_5,
            node_do_librarian_info,
            node_wait_6,
            node_do_investigator_info,
            node_wait_7,
            node_do_chef_info,
            node_wait_8,
            node_empath_moves,
            node_wait_9,
            node_end_first_night,
            node_wait_10
        ])
        
        #############################
        # Other Night
        #############################
        node_condition_other_night = NodeST_ConditionOtherNight("Check Other Night Condition", story_teller=self.story_teller)
        node_end_other_night = NodeST_EndOtherNight("End Other Night", story_teller=self.story_teller)
        node_nighttime.add_children([node_condition_other_night, node_end_other_night])

        #############################
        # Day Time
        #############################
        node_condition_day = NodeST_ConditionDay("Check Day Condition", story_teller=self.story_teller)
        node_call_townsquare = NodeST_CallTownSquare("Call Townsquare", story_teller=self.story_teller)
        node_daytime.add_children([node_condition_day, node_call_townsquare])

        #############################
        # Town Square
        #############################
        node_condition_townsquare = NodeST_ConditionTownSquare("Check TownSquare Condition", story_teller=self.story_teller)
        node_end_day = NodeST_EndDay("End Day", story_teller=self.story_teller)
        node_townsquare.add_children([node_condition_townsquare, node_end_day])

    def tick(self):
        """Tick the behavior tree once and return the status"""
        return self.root.tick_once()
