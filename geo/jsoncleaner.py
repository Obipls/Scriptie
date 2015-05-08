import json
import re
import sys
from pygeocoder import Geocoder


def main():
	with open('alerts_test.json') as data_file:
		alerts = json.load(data_file)
	
	for i in range(500):
		for alert in alerts:
			if alert["cause"] == []:
				alerts.remove(alert)

	for i in range(200):
		for alert in alerts:
			if  ":" not in ''.join(alert ["time"]):
				alerts.remove(alert)
	
	for i in range(400):
		for alert in alerts:
			if not re.search('[A-P]\s[0-9]', ''.join(alert ["cause"])):
				alerts.remove(alert)

	causeList=[]
	for alert in alerts:
		causeList.append(''.join(alert ["cause"]))
	causeSplitList=[]
	for cause in causeList:
		causeSplitList.append(cause.split())


	for cause in causeSplitList:
		address=str(cause[-3])," ",str(cause[-4]),", ",str(cause[-2])
		#print(''.join(address))
		try:
			results = Geocoder.geocode(''.join(address))
		except Exception,e:
			print("helaas")
	print(results)
		





			




if __name__ == '__main__':
	main()