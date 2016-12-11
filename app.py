from flask import Flask, render_template, request, redirect, url_for, session
import json, os, utils.maps, utils.foursquare, utils.movies, utils.events, utils.weather

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
    venueList.append(utils.movies.getMusic(zipcode))
    #music events section

    queries.append("events")
    venueList.append([utils.events.get_events(lat, lon, 5)])
    #events section
    
    the_weather = (utils.weather.main(lat, lon))
    #weather section
    
    return render_template("home.html", action_type="results", address=location, view_address=view_location, status="show_info", get_map=map_code, askIfCorrect=askIfCor, venues=venueList, q=queries, clat=lat, clon=lon, coords=venueList, view_weather=the_weather)



@app.route("/results/<query>/<lat>/<lon>", methods=["GET","POST"])
def detailed_search(query, lat, lon):
    #if query == "music":
        
    vList = []
    idList = []
    bigL = []
    venueList=(utils.movies.get_movies(lat, lon, query, 10))
    for ven in venueList:
        vList.append(ven[:3])
        idList.append(ven[3])
    i = 0
    length = len(venueList)
    return render_template("results.html", info=vList,clat=lat, clon = lon, photos=idList, bigL=venueList)



#print carts()

if __name__ == "__main__":
    app.debug = True
    app.run()
