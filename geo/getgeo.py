from geopy.geocoders import Nominatim
from jsoncleaner import *

def locationsnatcher(causes):
	locDict={}
	geolocator = Nominatim()
	for cause in causes:
		#print(cause)
		fullAddress=str(cause[-3])," ",str(cause[-4])," ",str(cause[-2])
		streetCity=str(cause[-3])," ",str(cause[-2])
		try:
			location = geolocator.geocode(''.join(fullAddress))
			locDict[location.address]=(location.latitude,location.longitude)
		except:	
			try:
				location = geolocator.geocode(''.join(streetCity))
				locDict[location.address]=(location.latitude,location.longitude)
			except Exception,e:
				print("{} has no location, sorry!".format(streetCity))
	return locDict

def main():
	causes=cleanup()
	coordinates=locationsnatcher(causes)
	print(coordinates)



if __name__ == '__main__':
	main()