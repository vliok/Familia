from flask import Flask, render_template, request, redirect, url_for, session
import urllib2, json, os, utils.maps, utils.foursquare, utils.movies

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
    queries = ["food", "coffee", "shops", "outdoors"]
    for q in queries:
        venueList.append(utils.foursquare.get_venues(lat, lon, q))

    #movies section
    queries.append("movie theaters")
    venueList.append(utils.movies.get_movies(lat, lon, 4))

    return render_template("home.html", action_type="results", address=location, view_address=view_location, status="show_info", get_map=map_code, askIfCorrect=askIfCor, venues=venueList, q=queries, clat=lat, clon=lon)


def carts():
    url = "./static/carts.json"
    f = open(url, "r").read()
    d = json.loads(f)
    carts = d["data"][0]
    return carts

print carts()
if __name__ == "__main__":
    app.debug = True
    app.run()
