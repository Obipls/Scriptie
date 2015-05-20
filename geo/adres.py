import csv
from collections import defaultdict
import pickle 

with open('adressen.csv') as csvfile:
	adressen = csv.reader(csvfile, delimiter=';')
	adresDict=defaultdict(list)
	for adres in adressen:
		if adres[2] != "Postbus":
				#if adres[2] not in adresDict.values()):
				adresDict[adres[1]].append(adres[2])
	
	for item in adresDict.values():
		 item=set(item)
		 item=list(item)
with open('adresses.pickle','wb') as f:
		pickle.dump(adresDict,f)