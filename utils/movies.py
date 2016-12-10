import urllib2, json, os, urllib

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
        print venue["venue"]["id"]
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

        
#print get_photos('4d49bf534a6d8eec89c92a2d')
get_movies(40.7179464,-74.0139052,"coffee",4)
