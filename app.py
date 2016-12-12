from flask import Flask, render_template, request, redirect, url_for, session
import json, os, utils.maps, utils.movies, utils.events, utils.weather #, utils.carts

app = Flask(__name__)


#status can either be - no_info, show_info, reenter





@app.route("/")
def home():
    return render_template("home.html", action_type="results", status="no_info")





@app.route("/results", methods=["GET","POST"])
def overview():
    try:
        #if getting geolocation automatically
        lat = float(request.form["lat"])
        lon = float(request.form["lon"])
        location = utils.maps.reverse_geo({'lat': lat, 'lng': lon})
        view_location = location.replace("+", " ") #making sure that it is defined
        view_location = view_location.replace("%2C", ",")
        askIfCor=True#a way for us to ask our user if their adress is correct
    except:
        #if manually typing address
        view_location=request.form["adress"]
        location = view_location.replace(" ", "+")
        askIfCor=False
        latlon = utils.maps.geo_loc(location)
        lat = latlon["lat"]
        lon = latlon["lng"]


    if(location == "" or location == " "):
        return render_template("home.html", action_type="results", address=location, view_address=view_location, status="reenter")

    map_code = utils.maps.get_map_query(location)

    venueList = []
    bigL = []
    queries = ["food", "coffee", "shops", "movies"]
    for q in queries:
        venueList.append(utils.movies.get_movies(lat, lon, q, 4))
    #movies section

    queries.append("music")
    zipcode = utils.maps.reverse_geo({'lat':float(lat), 'lng':float(lon)})[-12:-7]
    venueList.append(utils.movies.getMusicList(zipcode))
    #music events section

    queries.append("events")
    venueList.append([utils.events.get_events(lat, lon, 5)])
    #events section
    queries.append("carts")
    venueList.append(carts())
    the_weather = (utils.weather.main(lat, lon))
    #weather section
    
    return render_template("home.html", action_type="results", address=location, view_address=view_location, status="show_info", get_map=map_code, askIfCorrect=askIfCor, venues=venueList, q=queries, clat=lat, clon=lon, coords=venueList[0], view_weather=the_weather)



@app.route("/results/<query>/<lat>/<lon>", methods=["GET","POST"])
def detailed_search(query, lat, lon):
    vList = []
    idList = []
    bigL = []
    if query == "music":
        venueList=(utils.movies.getMusicList(utils.maps.reverse_geo({'lat':float(lat), 'lng':float(lon)})[-12:-7]))
        return render_template("results.html", info=venueList,clat=lat, clon = lon, photos=idList, bigL=venueList)

    if query=="carts":
        venueList = carts()
        return render_template("results.html", info=venueList,clat=lat, clon = lon, photos=idList, bigL=venueList, halal=True)
    
    venueList=(utils.movies.get_movies(lat, lon, query, 10))
    for ven in venueList:
        vList.append(ven[:3])
        idList.append(ven[3])

    #i = 0
    #length = len(venueList)
    return render_template("results.html", info=vList,clat=lat, clon = lon, photos=idList, bigL=venueList)


def carts():
    url = "carts.json"
    f = open(url, "r").read()
    d = json.loads(f)
    carts = d["data"][40005:40050]
    retL = []
    for c in carts:
        lat = c[-5]
        lng = c[-4]
        try:
            if len(lat) > 7:
                retL.append([c[0],float(lat),float(lng)])
        except:
            pass
    return retL
#print carts()

if __name__ == "__main__":
    app.debug = True
    app.run()
