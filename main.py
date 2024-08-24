from RPS_game import play, mrugesh, abbey, quincy, kris, human, random_player
from RPS import player
from unittest import main

print("Playing against Quincy:")
play(player, quincy, 1000)

print("Playing against Abbey:")
play(player, abbey, 1000)

print("Playing against Kris:")
play(player, kris, 1000)

print("Playing against Mrugesh:")
play(player, mrugesh, 1000)

# Uncomment to play interactively against a bot:
play(human, abbey, 20, verbose=True)

# Uncomment to play against a random bot:
play(human, random_player, 1000)

# Uncomment to run unit tests automatically
main(module='test_module', exit=False)
