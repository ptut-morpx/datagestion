from swissround.tournament.Player import Player
from random import gauss, randint
from math import log


class Generator:
	def __init__(self, ranking, n):
		self.n = n
		self.k = n//4
		self.expLambda = log(2)/2
		self.ranking = ranking
		if len(self.ranking) != n:
			self.ranking.append(Player("random", [0, 0, 0, 0]))
			for i in range(n-1):
				intelligence = [gauss(0, 1), gauss(0, 1), gauss(0, 1), gauss(0, 1)]
				self.ranking.append(Player(str(intelligence), intelligence))

	def evol(self):
		self.ranking = self.ranking[:self.n-self.k]

		for loop in range(self.k):
			toEvol = 0
			rand = randint(1, 3) % 3
			while toEvol < 7 and rand == 0:
				toEvol += 1
				rand = randint(1, 3) % 3

			newIntel = self.ranking[toEvol].intelligence
			for i in range(len(newIntel)):
				newIntel[i] = newIntel[i] + gauss(0, 1)
			self.ranking.append(Player(str(newIntel), newIntel))
