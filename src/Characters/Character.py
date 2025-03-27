class Character:

    def __init__(self, character_name, character_type, alignment):
        self.character_name = character_name
        self.character_type = character_type
        self.alignment = alignment
    
    def __str__(self):
        return self.character_name
    
    def __repr__(self):
        return self.character_name

    def GetPercievedCharacter(self):
        return self.character_name

    def TakeNightAction(self, action, player_brain):
        output = action.TakeAction()
        return output
    
    def TakeAction(self, action):
        return