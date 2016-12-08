import urllib2, json, os, urllib

def get_events(lat, lon, num):
    #url = "https://api.meetup.com/find/events?key=5648714275751c2a37271d242b5846&lon=-73.9859414&lat=40.713509699999996"

    new_lat = str(lat)
    new_lon = str(lon)
    
    url = "https://api.meetup.com/find/events?key=5648714275751c2a37271d242b5846&lon="+new_lon+"&lat="+new_lat
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    i=0;
    #print d[0]["name"]# there is way more info, we just need to seize it
    #print d[1]["name"]# there is way more info, we just need to seize it
    
    ret_list=[]

    i=0;

    while i<num:
        info = d[i]["name"]
        info
        ret_list.append(info)
        i+=1

    return ret_list
    
#https://api.meetup.com/find/events?key=5648714275751c2a37271d242b5846&lon=-73.9859414&lat=40.713509699999996
#print(get_events(40.713509699999996,-73.9859414))
