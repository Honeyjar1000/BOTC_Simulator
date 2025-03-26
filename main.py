from src.Game import Game
from src.Characters.EnumCharacter import Characters




game_instance = Game(player_count=15)
game_instance.GenerateGame()
game_instance.RunGame()

