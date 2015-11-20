import pickle, Geohash, geohash
from progressbar import ProgressBar

def lochasher(lines):
	hashDict = {}
	for line in lines:
		if type(line[1]) != tuple:
			hashed = Geohash.encode(round(float(line[0][0]),6),round(float(line[0][1]),6),7)
			hashDict.setdefault(hashed,[]).append(line)
		else:
			hashed = Geohash.encode(round(float(line[0][1]),6),round(float(line[0][0]),6),7)
			hashedneighbors = geohash.neighbors(hashed)
			hashedneighbors.append(hashed)
			hashDict.setdefault((' '.join(hashedneighbors),line[1]),[]).append(line)
	return hashDict

def locmatcher(tweets,alerts):
	matchDict={}
	pbar=ProgressBar()
	x=0
	for hashedtw in pbar(tweets):
		for hashedal in alerts:
			if  hashedtw in hashedal[0].split():
				matchDict.setdefault(hashedal[0],[]).append(hashedtw)
	return matchDict

def getvalues(tweets,alerts,matches):
	pbar=ProgressBar()
	taDict={}
	for alert in pbar(alerts):
		for match in matches:
			if alert[0] == match:
				alert=alerts.get(alert)[0]
				for tweethash in matches.get(match):
					tweet=tweets.get(tweethash)[0]
					taDict.setdefault(alert,[]).append(tweet)
	return(taDict)

def main():
	tweets = pickle.load(open('tweetlocs.pickle','rb'))
	alerts = pickle.load(open('geolocsall.pickle','rb'))
	hashedtweets = lochasher(tweets)
	with open('hashedtweets.pickle','wb') as f:
		pickle.dump(hashedtweets,f)
	hashedalerts = lochasher(alerts)
	with open('hashedalerts.pickle','wb') as f:
		pickle.dump(hashedalerts,f)
	matched=locmatcher(hashedtweets,hashedalerts)
	with open('matchedvalues.pickle','wb') as f:
		pickle.dump(matched,f)
	hashedtweets = pickle.load(open('hashedtweets.pickle','rb'))
	hashedalerts = pickle.load(open('hashedalerts.pickle','rb'))
	matched = pickle.load(open('matchedvalues.pickle','rb'))
	values=getvalues(hashedtweets,hashedalerts,matched)
	with open('allmatches.pickle','wb') as f:
		pickle.dump(values,f)

if __name__ == '__main__':
	main()