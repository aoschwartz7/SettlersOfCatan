import random

# Classes
# create class Hex so we can attribute board positions to the hexes we've created and then draw them to board
class Hex:
	def __init__(self, position, frequency, resource):
		self.position = position
		self.frequency = frequency
		self.resource = resource
	def printHex(self):
		print(self.position, self.frequency, self.resource)


class Board:
	emptyHexes = ['brick', 'brick', 'brick',
	'ore','ore', 'ore',
	'wheat','wheat','wheat','wheat',
	'wood','wood','wood','wood',
	'sheep','sheep','sheep','sheep',
	'desert']
	frequencies = [2, 3, 3, 4, 4, 5, 5, 6, 6, 8, 8, 9, 9, 10, 10, 11, 11, 12 ]

	def __init__(self):
		self.hexes = []
		self.createHexes()

	def createHexes(self):
		random.shuffle(self.frequencies)
		random.shuffle(self.emptyHexes)
		# ascribe Hex class properties to hex tiles
		for i in range(len(self.emptyHexes)):
			if self.emptyHexes[i] == 'desert':
				hex = Hex(i, -1, self.emptyHexes[i])
				self.frequencies.append(self.frequencies[i]) 	# make up for not using desert frequency
			else:
				hex = Hex(i, self.frequencies[i], self.emptyHexes[i])
			self.hexes.append(hex)

	def printHexes(self):
		for i in self.hexes:
			i.printHex()




# class for ascribing properties to all possible settlement junctures
class Settlement:
	def __init__(self, location, type, owner):
		pass
# class for ascribing properties to all possible city junctures
class City:
	def __init__(self, location, type, owner):
		pass

# class for ascribing properties to all possible road segments
class Road:
	def __init__(self, location, owner):
		pass

class DevelopmentCards:
	def __init__(self, owner):
		pass
