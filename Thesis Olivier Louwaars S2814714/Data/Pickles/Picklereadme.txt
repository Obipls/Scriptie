Toplevel:
alertstweets.pickle = dictionary with (key = message, date and time of alert,value = list of every corresponding tweet of the entire month with username and timestamp)
matchedvalues.pickle = dictionary with (key = hash of alert, value = list of geohashes of all corresponding tweets of the entire month)
allmatches.pickle = dictionary with (key = location, date and time of event, value = location and username of corresponding tweets of the entire month)
baseline.pickle = dictionary with (key = message, time and date of alert, value = list of tweets with username and timestamp of same day)
baselinetimes.pickle = dictionary with (key = message, time and date of alert, value = list of tweets with username and timestampof same time window (2 hours before, 3 hours after alert))

Map Tweets:
hashedtweets.pickle = dictionary with (key = geohash of tweetlocation, value = gps coordinate and username of tweet)
tweetlocs.pickle = dictionary with (key = gps coordinate of tweet, value = username and message of tweet)
tweettd.pickle = dictionary with (key = gps coordinate and username of tweet, value = time and date of tweet)

Map Alerts:
geolocsall.pickle = dictionary with (key = gps coordinate, time&date and retrieved adress of alert, value = alert)
hashedalerts.pickle = dictionary with (key = geohash of alertlocation with it's neighbours, value = time, date and gps location of alert)