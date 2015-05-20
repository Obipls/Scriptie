from geopy.geocoders import Nominatim
import pickle

def locationsnatcher(causes):

	locDict={}
	geoList=[]
	geolocator = Nominatim()
	x=0
	for cause in causes:
		fullAddress= ' '.join(causes.get(cause)[-1])
		geoList.append([cause,fullAddress])

	print(len(geoList))

	for loc in geoList[50000:]:
		location = geolocator.geocode(loc[-1], timeout=15)
		print(x)
		x+=1
		if location != None:
			locgeo=(location.latitude,location.longitude)
			locDict[(locgeo,loc[0])]=[location.address,causes.get(loc[0])[0]]	
	return locDict

def main():
	addressfile='causesaddr.pickle'
	addresses=pickle.load(open(addressfile, 'rb'))
	coordinates=locationsnatcher(addresses)
	print (len(coordinates))
	with open('geolocs13.pickle','wb') as f:
		pickle.dump(coordinates,f, protocol=0)
 


if __name__ == '__main__':
	main()