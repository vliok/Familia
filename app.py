from flask import Flask, render_template, request, redirect, url_for, session
import urllib2, json, os, utils.maps

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
    except:
        #if manually typing address
        location = request.form["adress"].replace(" ", "+")

    if(location == "" or location == " "):
        return render_template("home.html", action_type="results", address=location, status="reenter")

    map_code = utils.maps.get_map_query(location);

    return render_template("home.html", action_type="results", address=location, status="show_info", get_map=map_code)


if __name__ == "__main__":
    app.debug = True
    app.run()
