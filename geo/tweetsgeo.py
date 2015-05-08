import codecs
def main():
	textFile = codecs.open('tweets_hup.txt', 'r','utf-8')
	rawText = textFile.read().encode('utf-8')
	for line in rawText:
		print("hallo")

if __name__ == '__main__':
	main()