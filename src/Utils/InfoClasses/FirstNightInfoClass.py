
class FirstNightInfoClass:

    def __init__(self, data):
        self.data = data

    def __str__(self):
        s = str(self.data[1][0].player_name) + ' or ' + str(self.data[1][1].player_name)
        s += ' is the ' + self.data[0].name
        return s