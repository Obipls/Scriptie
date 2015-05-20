import pickle
import Geohash
import geohash

def lochasher(lines):
	hashDict = {}
	for line in lines:
		hashed = Geohash.encode(round(float(line[0][0]),6),round(float(line[0][1]),6),4)
		if len(line) >2:
			hashDict[line] = hashed
		else:
			hashedneighbors = geohash.neighbors(hashed)
			hashedneighbors.append(hashed)
			hashDict[line] = hashedneighbors
	return hashDict

def locmatcher(tweets,alerts):
	x=0
	for hashedal in alerts.values():
		print("Next Alert:",hashedal)
		for hashedtw in tweets.values():
			if hashedal in hashedtw:
				print("found")
				x+=1
	print(x)


def main():
	tweets = pickle.load(open('tweetlocs.pickle','rb'))
	alerts = pickle.load(open('alertlocsall.pickle','rb'))
	hashedtweets = lochasher(tweets)
	hashedalerts = lochasher(alerts)
	locmatcher(hashedtweets,hashedalerts)



if __name__ == '__main__':
	main()