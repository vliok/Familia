from flask import Flask, render_template, request, redirect, url_for, session
import urllib2, json, os, utils.maps

app = Flask(__name__)


#status can either be - no_info, show_info, reenter

@app.route("/")
def home():
    return render_template("home.html", action_type="results", status="no_info")

@app.route("/results", methods=["GET","POST"])
def overview():
    location = request.form["adress"]
    
    if(location == "" or location == " "):
        return render_template("home.html", action_type="results", address=location, status="reenter")

    map_code = utils.maps.get_map_querry(location);
    
    return render_template("home.html", action_type="results", address=location, status="show_info", get_map=map_code)


if __name__ == "__main__":
    app.debug = True
    app.run() 


