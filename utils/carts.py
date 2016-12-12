import json
def carts():
    url = "/carts.json"
    f = open(url, "r").read()
    d = json.loads(f)
    carts = d["data"][40000:40005]
    retL = []
    for c in carts:
        lat = c[-5]
        lng = c[-4]
        try:
            if len(lat) > 7:
                retL.append([c[0],str(lat),str(lng)])
        except:
            pass
    return retL

#print carts()
