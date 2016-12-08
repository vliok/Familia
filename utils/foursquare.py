import urllib2, json, os, urllib

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"


def get_venues(lat, lon, query, n):
    url = "https://api.foursquare.com/v2/venues/explore?ll=%s,%s&section=%s&oauth_token=%s" % (lat, lon, query, key)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    venues = d["response"]["groups"][0]["items"][:4]
    llist = []
    for v in venues:
        #vname = v["venue"]["categories"][0]["name"]
        #print v
        if n==0:
            venue = v["venue"]["name"]
            llist.append(venue)
        if n == 1:
            try:
                lat = v["venue"]["location"]["labeledLatLngs"][0]["lat"]
                lng = v["venue"]["location"]["labeledLatLngs"][0]["lng"]
            except:
                lat = 0
                lng = 0
            llist.append([lat,lng])
        #adress = v["venue"]["formattedAddress"]
    return llist[:4]

def carts():
    url = "../static/carts.json"
    f = open(url, "r").read()
    d = json.loads(f)
    carts = d["data"][44000:46000]
    retL = []
    for c in carts:
        lat = c[-5]
        lng = c[-4]
        try:
            if len(lat) > 7:
                retL.append([c[0],lat,lng])
        except:
            pass
    return retL

#print get_venues(40.1293612931,-73.1293512351, "shops",0)
