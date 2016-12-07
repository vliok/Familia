import urllib2, json, os, urllib

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"

def get_movies(lat,lon):
    url = "https://api.foursquare.com/v2/venues/explore?ll="+str(lat)+","+str(lon)+"&query=movie&limit=5&oauth_token="+key
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    d = d["response"]["groups"][0]["items"]
    for venue in d:
        print venue["venue"]["name"]

get_movies(40.3,-74)
