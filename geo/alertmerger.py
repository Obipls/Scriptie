import pickle
aDict= {}

for i in range(14):
	print(i)
	alertfile='geolocs'+str(i)+'.pickle'
	alerts=pickle.load(open(alertfile, 'rb'))

	for key in alerts.keys():
		aDict[key]=alerts.get(key)

with open('geolocsall.pickle','wb') as f:
		pickle.dump(aDict,f)
	

#pickle.load(open('alerts.pickle','rb'))