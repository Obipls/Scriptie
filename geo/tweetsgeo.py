import pickle
def gettweetlocs():

    tweetDict = {}
    with open("tweets.txt") as f:
    	for line in f:
			tweet = line.strip().split('\t')
			tweetgeo = tweet[1].split()
			tweetgeo = (tweetgeo[0],tweetgeo[1])
			tweetDict[tweetgeo,tweet[-2]]=tweet[-1]

	return tweetDict

def main():
	coordinates=gettweetlocs()
	with open('tweetlocs.pickle','wb') as f:
		pickle.dump(coordinates,f)

if __name__ == '__main__':
	main()