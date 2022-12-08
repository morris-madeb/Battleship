import os
import gameLogic
import player
import board

START_LOGO = """
__________         __    __  .__                .__    .__        
\______   \_____ _/  |__/  |_|  |   ____   _____|  |__ |__|_____  
 |    |  _/\__  \\   __\   __\  | _/ __ \ /  ___/  |  \|  \____ \ 
 |    |   \ / __ \|  |  |  | |  |_\  ___/ \___ \|   Y  \  |  |_> >
 |______  /(____  /__|  |__| |____/\___  >____  >___|  /__|   __/ 
        \/      \/                     \/     \/     \/   |__|    
                  
                  by Isaac Schertz and Morris Madeb
                  
                    press enter to begin the game\n"""

# collect names after clearing screen using system.os("clear")
# defines the starting function for the game
def start():
  os.system("clear")
  print(START_LOGO)
  input()
  os.system("clear")
  # collects player names once for infinite gameplay between the two (or until they finish a game and decide to end the game)
  p1 = player.Player(input(board.HEADER + "\nwhat is player 1's name?\n"))
  while len(p1.name) < 1:
    os.system("clear")
    p1 = player.Player(input(board.HEADER + "\nName is invalid\nwhat is player 1's name?\n"))

  os.system("clear")
  p2 = player.Player(input(board.HEADER + "\nwhat is player 2's name?\n"))
  while len(p2.name) < 1 or p1.name == p2.name:
    os.system("clear")
    p2 = player.Player(input(board.HEADER + "\nName is invalid\nwhat is player 2's name?\n"))

  # prints game logo and begins the game until it ends, then asks to play again
  while True:
    os.system("clear")
    print(START_LOGO)
    input()
    os.system("clear")
    
    gameLogic.Battleship(p1, p2)
    endGame = ""
    while endGame not in ["y", "n"]:
      endGame = input("would you like to play again? (y/n)\n")
    if endGame == "n":
      break
# Start menu with a title
# take input to begin game
# want to be able to play an infinite amount of games
