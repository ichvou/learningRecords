#encoding: utf-8

class IsLand():
	"""docstring for IsLand"""
	def __init__(self, n, preyCnt=0, predatorCnt=0):
		self.gridSize = n
		self.grid = []
		for i in range(n):
			row = [0]*n
			self.grid.append(row)
		# self.initAnimals(preyCnt, predatorCnt)
    


	def size(self):
		return self.gridSize

	def register(self,animal):
		x = animal.x
		y = animal.y

		self.grid[x][y] = animal

	def __str__(self):
		s = ""
		for j in range(self.gridSize-1,-1,-1):
			for i in range(self.gridSize):
				if not self.grid[i][j]:
					s += "%-2s" % '.' + " "
				else:
					s += "%-2s" % (str(self.grid[i][j])) + " "
			s += "\n"
		return s

class Animal(object):
	def __init__(self, island, x=0, y=0, s="A"):
		self.island = island
		self.name = s 
		self.x = x
		self.y = y

	def __str__(self):
		return self.name

	def position(self):
		return self.x, self.y


royale = IsLand(10,0,0)
# print(royale)
animal1 = Animal(island=royale,x=4,y=8,s='a1')
# print(animal1.x,animal1.y)
animal2 = Animal(island=royale,x=6,y=4,s='a2')
royale.register(animal1)
royale.register(animal2)
print(animal1.position())