import json
def carts():
    url = "../static/carts.json"
    f = open(url, "r").read()
    d = json.loads(f)
    carts = d["data"][40000:40050]
    retL = []
    for c in carts:
        lat = c[-5]
        lng = c[-4]
        try:
            if len(lat) > 7:
                retL.append([c[0],lat,lng])
        except:
            pass
    print retL

print carts()
