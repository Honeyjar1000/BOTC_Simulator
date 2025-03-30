from src.Game import Game

game_instance = Game(player_count=15, wait_duration=0.1)
game_instance.GenerateGame()
game_instance.RunGame()

