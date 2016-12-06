from flask import Flask, render_template, request, redirect, url_for, session
import urllib2, json, os

app = Flask(__name__)


#status can either be - no_info, show_info, reenter

@app.route("/")
def home():
    return render_template("home.html", action_type="results", status="no_info")

@app.route("/results", methods=["GET","POST"])
def overview():
    location = request.form["adress"]
    print(location)
    #NEED AFXN TO GO DOWN THE STR AND CHECK IF EACH OF THE elements are " "

    if(location == "" or location == " "):
        return render_template("home.html", action_type="results", address=location, status="reenter")

    map_code = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAJZ69TpmhYn_53GCf3f_UdTyu7TWAk4Mk&q="+location#"NewYork+NY"

    split_location=location.split(",")
    print(split_location)
    print(len(split_location))
    size=len(split_location)
    
    map_querry = ""+split_location[size-3]+"+"+split_location[size-2]+"+"+split_location[size-1]

    print(map_querry)

    #map_code = "https://www.google.com/maps/embed/v1/place?key=AIzaSyAJZ69TpmhYn_53GCf3f_UdTyu7TWAk4Mk&q="+map_querry
    
    return render_template("home.html", action_type="results", address=location, status="show_info", get_map=map_code)


if __name__ == "__main__":
    app.debug = True
    app.run() 


