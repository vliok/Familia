import urllib2, json, os, urllib, datetime
import maps

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"

"""
Args:
lat - latitude of original location
lon - longitude of original location
query - either food, shops, coffee, movie
lim - number of items to return

Return:
info from foursquare api in format of:
[
    [venue name, venue lat, venue lon, venue id, venue category, venue rating, reviews]
]
"""

def get_movies(lat,lon, query, lim):
    url = "https://api.foursquare.com/v2/venues/explore?ll="+str(lat)+","+str(lon)+"&query=" + query + "&limit="+str(lim)+"&oauth_token="+key
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    d = d["response"]["groups"][0]["items"]
    retList = []
    for venue in d:
        #print venue["venue"]["id"]
        try:
            retList.append([str(venue["venue"]["name"]), venue["venue"]["location"]["lat"], venue["venue"]["location"]["lng"], get_photos(venue["venue"]["id"]),  venue["venue"]['categories'][0]['name'], venue["venue"]['rating'], venue["tips"][0]["text"]])
        except:
            pass
    return retList[:lim]

"""
Args:
venueID - id of venue 

Return:
list of url of photos
"""

def get_photos(venueID):
    url = "https://api.foursquare.com/v2/venues/" + venueID + "/photos?oauth_token=" + key
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    photo = d["response"]['photos']["items"][0] # get one photo for now
    #photoL = []
    #for photo in d:
    url = photo["prefix"] + "200x200" + photo["suffix"]
     #   photoL.append(url)
    return url


"""
Args:
zipcode: zipcode of area
llen: len of list to return

Return:
list of events in artist id, name, location, and time starting format
"""
def get_music(zipcode):
    now = datetime.datetime.now()
    today = str(now.year) + '-' + str(now.month) + '-' + str(now.day) 
    url = "http://api.jambase.com/events?zipCode=" + str(zipcode) + "&radius=0&startDate=" + today +  "&page=0&api_key=2pqkwk3rb3crydcdh9dcy6rv"
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    d = d["Events"]
    retL = []
    for event in d:
        if today in event["Date"]:
            time = event["Date"][len(today) + 1:]
            retL.append([str(event["Artists"][0]["Id"]), str(event["Artists"][0]["Name"]), str(event["Venue"]["Address"]+" " +event["Venue"]["City"] + " " + event["Venue"]["State"]), str(time)])
        else:
            return retL

def getMusicList(zipcode):
    the_music = get_music(zipcode)
    musicL = []
    for a in the_music:
        latlon = maps.geo_loc(a[2])
        musicL.append([a[1], latlon['lat'], latlon['lng'], '', "concert", a[2], a[3]])
    return musicL

print getMusicList(10282)
#print get_photos('4d49bf534a6d8eec89c92a2d')
#print get_movies(40.7179464,-74.0139052,"coffee",4)
