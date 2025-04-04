import time
import py_trees
import random
from src.Characters.EnumCharacter import Characters

class NodeST_ExecutePlayer(py_trees.behaviour.Behaviour):
    def __init__(self, name, story_teller):
        self.story_teller = story_teller
        super(NodeST_ExecutePlayer, self).__init__(name)
        

    def update(self):
        player_list = list(self.story_teller.black_board.players.values())
        random_player = random.sample(player_list, 1)[0]
        self.story_teller.executed_today = random_player
        print(str(random_player) + " is executed!")
        if (type(random_player.character) == Characters.SAINT.value) and (random_player.b_is_poisoned == False) and (random_player.alive == True):
            self.story_teller.black_board.b_saint_executed = True
        random_player.alive = False

        # TODO the scarlet woman pass probably shouldn't be called here, where?
        self.story_teller.check_scarlet_woman_pass(random_player)
        return py_trees.common.Status.SUCCESS  # Return SUCCESS when wait is done
