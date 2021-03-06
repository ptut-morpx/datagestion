import pickle
import csv

def save(ranking, toID):
	with open("data/ranking.pickle", "wb") as r:
		pickle.dump(ranking[:32], r, pickle.HIGHEST_PROTOCOL)

	with open("data/winner.pickle", "wb") as w:
		pickle.dump(ranking[0], w, pickle.HIGHEST_PROTOCOL)

	with open("data/toID.int", "wb") as n:
		pickle.dump(toID, n, pickle.HIGHEST_PROTOCOL)


def logRank(ranking, toID):
	fileName = "data/log/log tournament n{}.csv".format(toID)
	with open(fileName, 'w', newline='') as csvfile:
		lineWriter = csv.writer(csvfile, dialect='unix')
		for player in ranking:
			lineWriter.writerow([player.name, player.score])


def retrieve():
	with open("data/ranking.pickle", "rb") as r:
		ranking = pickle.load(r)

	with open("data/toID.int", "rb") as n:
		toID = pickle.load(n)

	return ranking, toID
