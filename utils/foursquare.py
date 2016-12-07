import urllib2, json, os, urllib

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"


def get_venues(lat, lon, query):
    url = "https://api.foursquare.com/v2/venues/explore?ll=%s,%s&section=%s&oauth_token=%s" % (lat, lon, query, key)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    venues = d["response"]["groups"][0]["items"]
    llist = []
    for v in venues:
        #vname = v["venue"]["categories"][0]["name"]
        venue = v["venue"]["name"]
        #adress = v["venue"]["formattedAddress"]
        llist.append(venue)
    return llist
