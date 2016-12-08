import urllib2, json, urllib
key = "cc75d8edb8caaac081449e4871136ffe"
#https://api.darksky.net/forecast/[key]/[latitude],[longitude] (proper format)
url = "https://api.darksky.net/forecast/cc75d8edb8caaac081449e4871136ffe/40.7128,74.0059"

request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)
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
def backgrounder():
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "icon"):
                    
                    print d[key][k2]
                    return d[key][k2]

                
def temp():
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "data"):
#                    print d[key][k2]
                    for k3 in d[key][k2][0]:
                        if (k3 == "temperature"):
                            print d[key][k2][0][k3]
                    #return d[key][k2]

def humidity():
    for key in d:
        if (key == "hourly"):
            for k2 in d[key]:
                if (k2 == "data"):
#                    print d[key][k2][0]                                                                                                                                                                    
                    for k3 in d[key][k2][0]:
                        if (k3 == "humidity"):
                            print d[key][k2][0][k3]
                    #return d[key][k2]                                                                                                                                                                      


            
#backgrounder()
print()
print()
temp()
print 
print
humidity()
