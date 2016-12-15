import urllib2, json, os, urllib

key = "Q2ZBILRSORPXPLVBNGTX2BOBOYYBPPBBL4KBJDGKY0GEI35F&v=20161206"


def get_venues(lat, lon, query, n, num):
    url = "https://api.foursquare.com/v2/venues/explore?ll=%s,%s&section=%s&oauth_token=%s" % (lat, lon, query, key)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    venues = d["response"]["groups"][0]["items"]
    llist = []
    count = 0
    for v in venues:
        if n==0:
            count += 1
            venue = v["venue"]["name"]
            llist.append(venue)
        if n == 1:
            try:
                lat = v["venue"]["location"]["labeledLatLngs"][0]["lat"]
                lng = v["venue"]["location"]["labeledLatLngs"][0]["lng"]
                count += 1
                llist.append([lat,lng])
            except:
                lat = v["venue"]["location"]["lat"]
                lng = v["venue"]["location"]["lng"]
            #llist.append([lat,lng])
        if count == num:
            break
    return llist

mar = get_venues(40.008302846234, -73.972183912863, "food", 1, 10)
