import urllib2, json, urllib
key = "cc75d8edb8caaac081449e4871136ffe"
#https://api.darksky.net/forecast/[key]/[latitude],[longitude] (proper format)
url = "https://api.darksky.net/forecast/cc75d8edb8caaac081449e4871136ffe/42.3601,-71.0589"

request = urllib2.urlopen(url)
result = request.read()
d = json.loads(result)

for key in d:
    if (key == "hourly"): 
        for k2 in d[key]:
            print k2
            print "corresponds to"
            print d[key][k2]
            print 

#use icon to create a getBg fxn


