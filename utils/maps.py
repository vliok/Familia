import urllib2, json, os, urllib


key="AIzaSyAjRmGMuK_IQ2UUmYLHThc7JBdzZ4N22BQ"
keym="AIzaSyCIN3GS736I958G9695m5INnU7_vg4TLkE"

#get map query
def get_map_query(loc):
    googleurl = "https://www.google.com/maps/embed/v1/place?key=%s&q=%s" % (keym, loc)
    return googleurl

#given a dictionary with lng and lat to find approximate address
def reverse_geo(ldic):
        googleurl = "https://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&key=%s" % (ldic['lat'], ldic['lng'], key)
        request = urllib2.urlopen(googleurl)
        result = request.read()
        d = json.loads(result)
        rdic = d['results'][0]
        address = rdic['formatted_address']
        address = urllib.quote_plus(address)
        return address


def geo_loc(location):
#finds the longitude and latitude of a given location parameter using Google's Geocode API
#return format is a dictionary with longitude and latitude as keys
        loc = urllib.quote_plus(location)
        googleurl = "https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s" % (loc,key)
        request = urllib2.urlopen(googleurl)
        results = request.read()
        gd = json.loads(results) #dictionary
        if gd['status'] != "OK":
                return location+" is a bogus location! What are you thinking?"
        else:
                result_dic = gd['results'][0] #dictionary which is the first element in the results list
                geometry = result_dic['geometry'] #geometry is another dictionary
                loc = geometry['location'] #yet another dictionary
                return loc
