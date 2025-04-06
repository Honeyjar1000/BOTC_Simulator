from src.Characters.TownsFolk.Townsfolk import Townsfolk

class C_RavenKeeper(Townsfolk):
    def __init__(self):
        self.used = False
        super().__init__(character_name='RavenKeeper')