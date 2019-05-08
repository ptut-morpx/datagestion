import pickle
import csv


def save(ranking):
	with open("ranking.pickle", "wb") as r:
		pickle.dump(ranking[:32], r, pickle.HIGHEST_PROTOCOL)

	with open("winner.pickle", "wb") as w:
		pickle.dump(ranking[0], w, pickle.HIGHEST_PROTOCOL)

	with open("toID.int", "wb") as n:
		pickle.dump(toID, n, pickle.HIGHEST_PROTOCOL)


def logRank(ranking):
	fileName = "log tournament n{}.csv".format(toID)
	with open(fileName, 'w', newline='') as csvfile:
		lineWriter = csv.writer(csvfile, dialect='unix')
		for player in ranking:
			lineWriter.writerow([player.name, player.score])

	toID += 1


def retrieve():
	with open("ranking.pickle", "rb") as r:
		ranking = pickle.load(r)

	with open("toID.int", "rb") as n:
		toID = pickle.load(n)

	return ranking
