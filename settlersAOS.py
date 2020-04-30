# Repo: https://github.com/aoschwartz7/SettlersOfCatan
#
# TODOs
# create dice roller and establish turn-based system
# should we create player-specific lists of their board piece inventories? I.e. player 1 has a total number of the following pieces for board placements: 5 settlements, 4 cities, 15 roads
#
# extra) one fun mod (Denali's) could be to change size of hex depending on total die roll frequency
#
#
#
# Constants: Resources (Ore, Sheep, Wheat, Brick, Wood), Player Colors
# Classes: Board, Hex, Settlement, Road, City, Development Cards, Player
# Functions: hexTile, hexCorner


# Constants

import random
from settlersClasses import Hex, Board

players = ['p1', 'p2', 'p3', 'p4']

# (RGB colors for GUI)
brickColor = (255, 0, 0)
oreColor = (190, 190, 190)
wheatColor = (255, 215, 0)
sheepColor = (124, 252, 0)
woodColor = (0, 100, 0)
desertColor = (139, 69, 19)

# developmentCards = [ 'roadBuilding', 'roadBuilding',
# 'yearPlenty', 'yearPlenty',
# 'monopoly', 'monopoly',
# 'victoryPoint','victoryPoint','victoryPoint','victoryPoint','victoryPoint',
# 'knight','knight','knight','knight','knight','knight','knight','knight','knight','knight','knight','knight','knight']

# random.shuffle(developmentCards)





# list of all possible settlement/city locations
# GUI PART: once hexes are drawn, we can identify where on screen buildingLoc are using pygame 'on-click' method that reveals mouse click coordinates
buildingLoc = [ ]

# list of all possible road locations
# GUI PART: once hexes are drawn, we can identify where on the screen roadLoc are using pygame 'on-click' method that reveals mouse click coordinates
roadLoc = [ ]


# Functions

def diceRoller():
	dice1 = random.sample(1,6)
	dice2 = random.sample(1,6)
	rollSum = dice1+dice2
	return rollSum
def main():
	board = Board()
	board.printHexes()


if __name__ == '__main__':
	main()
