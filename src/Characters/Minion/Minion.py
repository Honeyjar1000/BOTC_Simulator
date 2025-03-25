
from src.Characters.Character import Character


class Minion(Character):

    def __init__(self, character_name):
        super().__init__(character_name=character_name, character_type='Minion', alignment='Evil')

    