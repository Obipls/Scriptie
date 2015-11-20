import nltk.metrics, sys, pickle, random
from itertools import chain
from tabulate import tabulate
from collections import Counter,defaultdict
from nltk import word_tokenize as wordToks
from nltk.classify import NaiveBayesClassifier as NBC, accuracy


reload(sys)
sys.setdefaultencoding("utf-8")

#http://www.laurentluce.com/posts/twitter-sentiment-analysis-using-python-and-nltk/
#http://streamhacker.com/2010/05/17/text-classification-sentiment-analysis-precision-recall/

def getfeatures(tweet,testingSet):
	featureDict ={}
	tweetTokens = set(wordToks(tweet))
	for word in testingSet:				
		if word in tweetTokens:
			featureDict[word] = True
		else:
			featureDict[word] = False	
	return featureDict

def classify():
	tweetSet = set()
	negtweetSet=set()
	for annotated in open("dagannotatie1.txt"):
		tweet = annotated.strip().split("\t")
		if len(tweet) == 4:
			if tweet[3].strip() is '0':
				negtweetSet.add((tweet[1], tweet[3]))
			else:
				tweetSet.add((tweet[1], tweet[3]))
	tweetSet.update(random.sample(negtweetSet,150))

	wordSet = chain(*[nltk.word_tokenize(i[0]) for i in tweetSet])
	wordAmount = Counter(wordSet)
	testingSet = set([word for word, n in wordAmount.most_common(250)])

	featureList = []
	for tweet, tag in tweetSet:
		featureDict = getfeatures(tweet,testingSet)
		featureList.append((featureDict,tag))	
	
	divider = int(0.8*len(featureList))
	trainTweets = featureList[:divider]
	testTweets = featureList[divider:]	
	classifier = NBC.train(trainTweets)
	print(accuracy(classifier,testTweets))

	ref = []
	tagged = []
	for f,e in testTweets:
		ref.append(e)
		tagged.append(classifier.classify(f))
	cm = nltk.ConfusionMatrix(ref,tagged)
	print(cm.pretty_format(sort_by_count=True, show_percents=True, truncate=9))




	refsets = defaultdict(set)
	taggedsets = defaultdict(set)
	for i, (feats, label) in enumerate(testTweets):
		refsets[label.strip()].add(i)
		observed = classifier.classify(feats)
		taggedsets[observed.strip()].add(i)


	table = [["Precision", "Recall", "F-score"], ["Positive", nltk.metrics.precision(refsets['1'], taggedsets['1']), nltk.metrics.recall(refsets['1'], taggedsets['1']), nltk.metrics.f_measure(refsets['1'], taggedsets['1'])],["Negative", nltk.metrics.precision(refsets['0'], taggedsets['0']), nltk.metrics.recall(refsets['0'], taggedsets['0']), nltk.metrics.f_measure(refsets['0'], taggedsets['0'])]]
	print(tabulate(table,headers="firstrow",tablefmt="plain"))


	print 'pos precision:', nltk.metrics.precision(refsets['1'], taggedsets['1'])
	print 'pos recall:', nltk.metrics.recall(refsets['1'], taggedsets['1'])
	print 'pos F-measure:', nltk.metrics.f_measure(refsets['1'], taggedsets['1'])
	print 'neg precision:', nltk.metrics.precision(refsets['0'], taggedsets['0'])
	print 'neg recall:', nltk.metrics.recall(refsets['0'], taggedsets['0'])
	print 'neg F-measure:', nltk.metrics.f_measure(refsets['0'], taggedsets['0'])
	print("\n")






	#test = 'HAARLEM : Haarlem , Pleiadenstraat , politie heeft zaak snel onderzocht , bleek een misverstand . Bedankt voor uw me http://t.co/4St2S5387r'
	#chances = classifier.prob_classify(getfeatures(test, testingSet))
	#for label in chances.samples():
	#	print("%s: %f" % (label, chances.prob(label)))
	print("informative features are: {}".format(classifier.show_most_informative_features()))



if __name__ == '__main__':
	classify()