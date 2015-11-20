import json, re, nltk, pickle
from nltk.tag.stanford import NERTagger
from collections import Counter

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def cleanup():

	adressfile='adresses.pickle'
	adresses=pickle.load(open(adressfile, 'rb'))

	with open('aprilp2000.json') as data_file:
		alerts = json.load(data_file)
	print("Linecount = {}".format(len(alerts)))
	
	# Remove all empty causes from the list of alerts
	alerts = [d for d in alerts if d.get('cause') != []]
	print("Empty cases removed, linecount = {}".format(len(alerts)))
	
	# Remove all alerts or other lines without a time
	alerts = [d for d in alerts if ':' in ''.join(d.get('time'))] 
	print("Empty timestamps removed, linecount = {}".format(len(alerts)))
	
	# Remove all alerts without a priority index (Capital letter followed by a space and one number)
	alerts = [d for d in alerts if re.search('[A-P]:?\s?[0-9]', ''.join(d.get('cause')))]
	print("No priority entries removed, linecount = {}".format(len(alerts)))

	print(len(alerts))

	# Gather all causes in 1 list for geosnatcher
	causes= [d.split() for d in [''.join(d) for d in [d.get('date')+[" "]+d.get('time')+[" "]+d.get('cause') for d in alerts]]]
	print("List created")

	causeDict = {}
	for cause in causes:
		for i,token in enumerate(cause):
			if str(token) in adresses.keys():
				city=token
				for j in range(len(cause)-1):
					if cause[j] in adresses.get(token):
						street=cause[j]
						if RepresentsInt(cause[j+1]) == True:
							if int(cause[j+1]) < 100:
								adress=[str(cause[j+1]),str(street),str(city)]
								causeDict[(cause[0],cause[1])]=[cause[2:],adress]
						else:
							adress=[str(street),str(city)]
							causeDict[(cause[0],cause[1])]=[cause[2:],adress]
	#with open('causesaddr.pickle','wb') as f:
	#	pickle.dump(causeDict,f)

cleanup()