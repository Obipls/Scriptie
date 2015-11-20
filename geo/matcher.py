import pickle, random
from collections import Counter
from progressbar import ProgressBar
from datetime import *

def matcher():
	pbar=ProgressBar()
	textDict={}
	matches = pickle.load(open('allmatches.pickle','rb'))
	alerts = pickle.load(open('geolocsall.pickle','rb'))
	tweets = pickle.load(open('tweetlocs.pickle','rb'))
	tweetmeta = pickle.load(open('tweettd.pickle', 'rb'))

	for match in pbar(matches):
		key=(' '.join(alerts.get(match)[1]),match[1])
		tweetkeys=set(matches.get(match))
		for tkey in tweetkeys:
			value=tweets.get(tkey),tkey[1],tweetmeta.get(tkey)[0]
			textDict.setdefault(key,[]).append(value)

	return textDict


def comparedays():
	texts = pickle.load(open('alertstweets.pickle','rb'))
	print(len(texts))
	samedaytexts={}
	for alert, tweets in texts.items():
		for tweet in tweets:
			tweetdate=tweet[-1][8]+tweet[-1][9]+tweet[-1][7]+tweet[-1][5]+tweet[-1][6]+tweet[-1][4]+tweet[-1][2]+tweet[-1][3]
			if str(alert[1][0]) == tweetdate:
				samedaytexts.setdefault(alert,[]).append(tweet)
	print(len(samedaytexts))
	return samedaytexts

def comparetimes():
	texts = pickle.load(open('alertstweets.pickle','rb'))
	x=0
	sametimetexts = {}
	for alert in texts:	
		adate=alert[-1][0].split('-')
		atime=str(alert[-1][1]).split(':')
		atimestamp=datetime(int("20"+adate[2]),int(adate[1]),int(adate[0]),int(atime[0]),int(atime[1]))
		atimestampmin=atimestamp-timedelta(hours=2)
		atimestampmax=atimestamp+timedelta(hours=3)
		for tweet in texts.get(alert):
			ttime=tweet[-1].split()[1].split(':')
			tdate=tweet[-1].split()[0].split('-')
			ttimestamp=datetime(int(tdate[0]),int(tdate[1]),int(tdate[2]),int(ttime[0]),int(ttime[1]))
			if ttimestamp > atimestampmin and ttimestamp<atimestampmax:
				sametimetexts.setdefault(alert,[]).append(tweet)

	print(len(sametimetexts))
	return sametimetexts


def getannodata():
	texts = pickle.load(open('baselinetimes.pickle','rb'))

	for x,match in enumerate(random.sample(texts,20)):
		print (str(x+1)+'\t'+match[0])
		for y,tweet in enumerate(texts.get(match)):
			print (str(y+1)+'\t'+tweet[0]+'\t'+tweet[1]+'\t0')





if __name__ == '__main__':
	#texts=matcher()
	#with open('alertstweets.pickle','wb') as f:
	#	pickle.dump(texts,f)
	#samedays=comparedays()
	#with open('baseline.pickle','wb') as f:
	#	pickle.dump(samedays,f)
	#
	#sametimes=comparetimes()
	#with open('baselinetimes.pickle','wb') as f:
	#	pickle.dump(sametimes,f)
	getannodata()
