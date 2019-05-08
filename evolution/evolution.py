from tournament.Player import Player
from random import gauss, randint
from math import log


class Generator:
	def __init__(self, ranking, n):
		self.n = n
		self.k = n//4
		self.expLambda = log(2)/2
		ranking.append(Player("random", None))
		for i in range(n-1):
			intelligence = [gauss(), gauss(), gauss(), gauss()]
			ranking.append(Player(str(intelligence), intelligence))

	def evol(self, ranking):
		ranking = ranking[:self.n-self.k]

		for i in range(self.k):
			toEvol = 0
			rand = randint(1, 3) % 3
			while toEvol < 7 and rand == 0:
				toEvol += 1
				rand = randint(1, 3) % 3

			newIntel = ranking[toEvol].intelligence
			for i in range(len(newIntel)):
				newIntel[i] = newIntel[i] + gauss()
			ranking.append(Player(str(newIntel), newIntel))
