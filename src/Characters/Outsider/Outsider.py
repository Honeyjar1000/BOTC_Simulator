from src.Characters import Character


class Outsider(Character):
    def __init__(self, character_name):
        super().__init__(character_name=character_name, character_type='Outsider', alignment='Good')