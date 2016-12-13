import urllib2, json, os, urllib

key = "5648714275751c2a37271d242b5846"

#opens and returns a dict
def opener(lat, lon):
    url = "https://api.meetup.com/find/events?key="+key+"&lon="+lon+"&lat="+lat
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    return d

#returns a list holding a list of the importnat info about events
#each elemnet in the big list corresponds to 1 event
#in each element there is 1 list, this list holds:
#in the following order->
#
#the name of teh event
#the description of the event
#the lat and lon of the event-if there is any
#photo for the event, no event that I have seen has this
def get_events(lat, lon, num):
    new_lat = str(lat)
    new_lon = str(lon)

    d = opener(new_lat, new_lon)

    name = get_events_name(new_lat, new_lon, num, d)
    desc = get_events_description(new_lat, new_lon, num, d)
    lat_lon = get_events_lat_lon(new_lat, new_lon, num, d)
    photo = get_events_photo(new_lat, new_lon, num, d)
    
    ret_list=[]
    i=0

    while i<num:
        info = []
        info.append(name[i])
        info.append(desc[i])
        info.append(lat_lon[i])
        info.append(photo[i])
        
        ret_list.append(info)
        i+=1

    return ret_list



def get_events_name(lat, lon, num, d):
    new_lat = str(lat)
    new_lon = str(lon)

    #d = opener(new_lat, new_lon)
    
    ret_list=[]
    i=0

    while i<num:
        info = d[i]["name"]
        ret_list.append(info)
        i+=1

    return ret_list


#if the event has a description it is returned, else, "NO DESCRIPTION"
#the values are passed in alist, size determined by n
def get_events_description(lat, lon, num, d):
    new_lat = str(lat)
    new_lon = str(lon)

    #d = opener(new_lat, new_lon)
    
    ret_list=[]
    i=0

    while i<num:
        try:
            info = d[i]["description"]
        except:
            info = "NO DESCRIPTION"
        ret_list.append(info)          
        i+=1
        
    return ret_list

#returns the lat and lon as one element in a list,
#returned in thr following order: ["lat1,lon1", "lat2,lon2"]
#it is passed as a str, so one must parse at the comma and then
#turn the str into an int
def get_events_lat_lon(lat, lon, num, d):
    new_lat = str(lat)
    new_lon = str(lon)

    #d = opener(new_lat, new_lon)
    
    ret_list=[]
    i=0
    
    while i<num:
        try:
            info = str(d[i]["venue"]["lat"])+","+str(d[i]["venue"]["lon"])
        except:
            info = "NO LAT, NO LON"
        ret_list.append(info)          
        i+=1
        
    return ret_list

#ALMOST NO ONE HAS A PHOTO< WE SHOULD NOT USE THIS
def get_events_photo(lat, lon, num, d):
    new_lat = str(lat)
    new_lon = str(lon)

    #d = opener(new_lat, new_lon)
    
    ret_list=[]
    i=0

    while i<num:
        try:
            info = str(d[i]["photo_album"])+","+str(d[i]["photo_album"])
        except:
            info = "NO PHOTO"
        ret_list.append(info)          
        i+=1
        
    return ret_list


#print(get_events_photo(40.713509699999996,-73.9859414, 10))
#print(get_events_lat_lon(40.713509699999996,-73.9859414, 10))
#print(get_events(40.713509699999996,-73.9859414, 10))
#print(get_events_description(40.713509699999996,-73.9859414, 10))
#https://api.meetup.com/find/events?key=5648714275751c2a37271d242b5846&lon=-73.9859414&lat=40.713509699999996
#print(get_events(40.713509699999996,-73.9859414,5))
