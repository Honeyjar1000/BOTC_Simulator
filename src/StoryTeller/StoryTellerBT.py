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
from src.StoryTeller.BTNodes.NodeST_SpyMoves import NodeST_SpyMoves
from src.StoryTeller.BTNodes.NodeST_EmpathMove import NodeST_EmpathMove
from src.StoryTeller.BTNodes.NodeST_FortuneTellerMove import NodeST_FortuneTellerMove
from src.StoryTeller.BTNodes.NodeST_Butler import NodeST_Butler
from src.StoryTeller.BTNodes.NodeST_MonkMove import NodeST_MonkMove
from src.StoryTeller.BTNodes.NodeST_Wait import NodeST_Wait
from src.StoryTeller.BTNodes.NodeST_ExecutePlayer import NodeST_ExecutePlayer
from src.StoryTeller.BTNodes.NodeST_DemonMove import NodeST_DemonMove
from src.StoryTeller.BTNodes.NodeST_RavenKeeperMove import NodeST_RavenMove


class StoryTellerBT:
    def __init__(self, story_teller, wait_duration=1):
        self.story_teller = story_teller
        self.wait_duration = wait_duration
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
        node_spy_moves = NodeST_SpyMoves("Spy", story_teller=self.story_teller)
        node_wait_5 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Washer Woman
        node_do_washer_woman_info = NodeST_WasherWomanInfo("First Night Washer Woman Info", story_teller=self.story_teller)
        node_wait_6 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Librarian
        node_do_librarian_info = NodeST_LibrarianInfo("First Night Librarian Info", story_teller=self.story_teller)
        node_wait_7 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Investigator
        node_do_investigator_info = NodeST_InvestigatorInfo("First Night Investigator Info", story_teller=self.story_teller)
        node_wait_8 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Chef
        node_do_chef_info = NodeST_ChefInfo("First Night Chef Info", story_teller=self.story_teller)
        node_wait_9 = NodeST_Wait("Wait", duration=self.wait_duration)
        
        # Empath
        node_empath_moves = NodeST_EmpathMove("Empath Moves", story_teller=self.story_teller)
        node_wait_10 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Fortune Teller
        node_fortune_teller_moves = NodeST_FortuneTellerMove("Fortune Teller Moves", story_teller=self.story_teller)
        node_wait_11 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Butler
        node_butler_moves = NodeST_Butler("Butler Moves", story_teller=self.story_teller)
        node_wait_12 = NodeST_Wait("Wait", duration=self.wait_duration)

        node_end_first_night = NodeST_EndFirstNight("End First Night", story_teller=self.story_teller)
        node_wait_13 = NodeST_Wait("Wait", duration=self.wait_duration)

        node_first_nighttime.add_children([
            node_condition_first_night, 
            node_wait_1,
            node_first_night_minion_info,
            node_wait_2, 
            node_first_night_demon_info, 
            node_wait_3,
            node_poisoner_moves,
            node_wait_4,
            node_spy_moves,
            node_wait_5,
            node_do_washer_woman_info,
            node_wait_6,
            node_do_librarian_info,
            node_wait_7,
            node_do_investigator_info,
            node_wait_8,
            node_do_chef_info,
            node_wait_9,
            node_empath_moves,
            node_wait_10,
            node_fortune_teller_moves,
            node_wait_11,
            node_butler_moves,
            node_wait_12,
            node_end_first_night,
            node_wait_13
        ])
        
        #############################
        # Other Night
        #############################
        node_condition_other_night = NodeST_ConditionOtherNight("Check Other Night Condition", story_teller=self.story_teller)
        
        # Poisoner
        node_poisoner_moves_2 = NodeST_PoisonerMove("Poisoner Moves", story_teller=self.story_teller)
        node_wait_14 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Monk
        node_poisoner_moves_2 = NodeST_MonkMove("Monk Moves", story_teller=self.story_teller)
        node_wait_14 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Spy
        node_spy_moves_2 = NodeST_SpyMoves("Spy Moves", story_teller=self.story_teller)
        node_wait_15 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Imp
        node_imp_moves = NodeST_DemonMove("Imp Moves", story_teller=self.story_teller)
        node_wait_16 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Raven Keeper
        node_raven_keeper_moves = NodeST_RavenMove("Raven Keeper Moves", story_teller=self.story_teller)
        node_wait_17 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Empath
        node_empath_moves_2 = NodeST_EmpathMove("Empath Moves", story_teller=self.story_teller)
        node_wait_18 = NodeST_Wait("Wait", duration=self.wait_duration)
    
        # Fortune Teller
        node_fortune_teller_moves_2 = NodeST_FortuneTellerMove("Fortune Teller Moves", story_teller=self.story_teller)
        node_wait_19 = NodeST_Wait("Wait", duration=self.wait_duration)

        # Butler
        node_butler_moves_2 = NodeST_Butler("Butler Moves", story_teller=self.story_teller)
        node_wait_20 = NodeST_Wait("Wait", duration=self.wait_duration)

        node_end_other_night = NodeST_EndOtherNight("End Other Night", story_teller=self.story_teller)
        node_nighttime.add_children([
            node_condition_other_night, 
            node_poisoner_moves_2,
            node_wait_14,
            node_spy_moves_2,
            node_wait_15,
            node_imp_moves,
            node_wait_16,
            node_raven_keeper_moves,
            node_wait_17,
            node_empath_moves_2,
            node_wait_18,
            node_fortune_teller_moves_2,
            node_wait_19,
            node_butler_moves_2,
            node_wait_20,
            node_end_other_night])

        #############################
        # Day Time
        #############################
        node_condition_day = NodeST_ConditionDay("Check Day Condition", story_teller=self.story_teller)
        node_wait_day = NodeST_Wait("Wait", duration=0.5)
        node_call_townsquare = NodeST_CallTownSquare("Call Townsquare", story_teller=self.story_teller)
        node_daytime.add_children([
            node_condition_day, 
            node_wait_day, 
            node_call_townsquare])

        #############################
        # Town Square
        #############################
        node_condition_townsquare = NodeST_ConditionTownSquare("Check TownSquare Condition", story_teller=self.story_teller)
        node_wait_townsquare = NodeST_Wait("Wait", duration=0.5)
        node_execute_player = NodeST_ExecutePlayer("Execute player", story_teller=self.story_teller)
        node_end_day = NodeST_EndDay("End Day", story_teller=self.story_teller)
        
        node_townsquare.add_children([
            node_condition_townsquare, 
            node_wait_townsquare, 
            node_execute_player,
            node_end_day])
        
    def tick(self):
        """Tick the behavior tree once and return the status"""
        return self.root.tick_once()
