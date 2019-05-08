import pickle


def save(ranking):
	with open("ranking.pickle", "wb") as r:
		pickle.dump(ranking[:32], r, pickle.HIGHEST_PROTOCOL)

	with open("winner.pickle", "wb") as w:
		pickle.dump(ranking[0], w, pickle.HIGHEST_PROTOCOL)


def retrieve():
	with open("ranking.pickle", "rb") as r:
		temp = pickle.load(r)

	return temp
