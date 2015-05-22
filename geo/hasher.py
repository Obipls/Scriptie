import pickle, Geohash, geohash
from progressbar import ProgressBar
from collections import defaultdict

def lochasher(lines):
	hashDict = {}
	for line in lines:
		if type(line[1]) == tuple:
			hashed = Geohash.encode(round(float(line[0][0]),6),round(float(line[0][1]),6),7)
			hashDict[line] = hashed
		else:
			hashed = Geohash.encode(round(float(line[0][1]),6),round(float(line[0][0]),6),7)
			hashedneighbors = geohash.neighbors(hashed)
			hashedneighbors.append(hashed)
			hashDict[line] = hashedneighbors
	return hashDict

def locmatcher(tweets,alerts):
	matchDict=defaultdict(list)
	pbar=ProgressBar()
	x=0
	for hashedal in pbar(alerts):
		for hashedtw in tweets:
			if alerts.get(hashedal) in tweets.get(hashedtw):
				matchDict[hashedal]=hashedtw
				x+=1

	print(x)
	return matchDict


def main():
	tweets = pickle.load(open('tweetlocs.pickle','rb'))
	print("Tweets gathered, {}".format(len(tweets)))
	alerts = pickle.load(open('geolocsall.pickle','rb'))
	print("Alerts gathered, {}".format(len(alerts)))
	hashedtweets = lochasher(tweets)
	print("Tweets hashed, {}".format(len(hashedtweets)))
	hashedalerts = lochasher(alerts)
	print("Tweets hashed, {}".format(len(hashedalerts)))
	matched=locmatcher(hashedtweets,hashedalerts)
	with open('matched.pickle','wb') as f:
		pickle.dump(matched,f)



if __name__ == '__main__':
	main()