import urllib2, json, os, urllib

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"

def get_movies(lat,lon, query, lim):
    url = "https://api.foursquare.com/v2/venues/explore?ll="+str(lat)+","+str(lon)+"&query=" + query + "&limit="+str(lim)+"&oauth_token="+key
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    d = d["response"]["groups"][0]["items"]
    retList = []
    for venue in d:
        retList.append([str(venue["venue"]["name"]), venue["venue"]["location"]["lat"], venue["venue"]["location"]["lng"]])
    return retList[:lim]


#print get_movies(40.7179464,-74.0139052,"food",10)
