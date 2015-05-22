import pickle
from collections import Counter
from collections import defaultdict

def matcher():
	textDict={}
	matches = pickle.load(open('matched.pickle','rb'))
	alerts = pickle.load(open('geolocsall.pickle','rb'))
	tweets = pickle.load(open('tweetlocs.pickle','rb'))
	tweetmeta = pickle.load(open('tweettd.pickle', 'rb'))

	for match in matches:
		key=(' '.join(alerts.get(match)[1]),match[1])
		textDict[key]=(tweets.get(matches.get(match)),matches.get(match)[1],tweetmeta.get(matches.get(match))[0])
	return textDict


def comparedays():
	texts = pickle.load(open('textmatches.pickle','rb'))
	samedaytexts={}
	for text in texts:
		tweetdate=texts.get(text)[-1][8]+texts.get(text)[-1][9]+texts.get(text)[-1][7]+texts.get(text)[-1][5]+texts.get(text)[-1][6]+texts.get(text)[-1][4]+texts.get(text)[-1][2]+texts.get(text)[-1][3]

		if str(text[1][0]) == tweetdate:
			samedaytexts[str(text)]=texts.get(text)
	return samedaytexts


if __name__ == '__main__':
	#texts=matcher()
	#with open('textmatches.pickle','wb') as f:
	#	pickle.dump(texts,f)
	samedays=comparedays()
	print(samedays)
