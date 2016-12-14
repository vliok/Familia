import urllib2, json, urllib
key = "cc75d8edb8caaac081449e4871136ffe"
#https://api.darksky.net/forecast/[key]/[latitude],[longitude] (proper format)
def setup(lon, lat):
    url = "https://api.darksky.net/forecast/cc75d8edb8caaac081449e4871136ffe/"+ str(lon) + "," + str(lat)
    request = urllib2.urlopen(url)
    result = request.read()
    d = json.loads(result)
    return d

'''
for key in d:
    if (key == "hourly"):
        for k2 in d[key]:
            print k2
            print "corresponds to"
            print d[key][k2]
            print
#use icon to create a getBg fxn

'''
def backgrounder(lon, lat):
    d = setup(lon, lat)
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "icon"):

                    #print d[key][k2]
                    return d[key][k2]


def temp(lon, lat):
    d = setup(lon, lat)
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "data"):
#                    print d[key][k2]
                    for k3 in d[key][k2][0]:
                        if (k3 == "temperature"):
                            return d[key][k2][0][k3]
                    #return d[key][k2]

def humidity(lon, lat):
    d = setup(lon,lat)
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "data"):
#                    print d[key][k2][0]
                    for k3 in d[key][k2][0]:
                        if (k3 == "humidity"):
                            return d[key][k2][0][k3]
                    #return d[key][k2]
def main(lon, lat):
    a = backgrounder(lon, lat)
    b = str(temp(lon, lat))
    c = str(humidity(lon, lat))

    L = []
    L.append(a)
    L.append(b)
    L.append(c)

    return L




#backgrounder()
#backgrounder(74, 10)
#print()
#print()
#temp(74, 10)

#print
#humidity(74, 10)
#print(main(74,10))
