#Call: python downloader.py | gettweets.py > output.txt

import os
import sys

def main():
	#for i in range(4,10):
	#	gettweets= "zcat /net/corpora/twitter2/Tweets/2014/0"+str(i)+"/2014???????.out.gz | /net/corpora/twitter2/tools/tweet2tab -i date coordinates place user words"
	#	os.system(gettweets)
	
	#for i in range(10,13):
	#	gettweets= "zcat /net/corpora/twitter2/Tweets/2014/"+str(i)+"/2014???????.out.gz | /net/corpora/twitter2/tools/tweet2tab -i date coordinates place user words"
	#	os.system(gettweets)
		
	for i in range (4,6):
		gettweets= "zcat /net/corpora/twitter2/Tweets/2015/0"+str(i)+"/2015???????.out.gz | /net/corpora/twitter2/tools/tweet2tab -i date coordinates place user words"
		os.system(gettweets)

main()
