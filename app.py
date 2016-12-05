from flask import Flask, render_template, request, redirect, url_for, session
import urllib2, json, os

app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html", action_type="results", permission=False)

@app.route("/results", methods=["POST"])
def overview():
    location = request.form["adress"]
    print("working")
    return render_template("home.html", action_type="results", adress=location, permission=True)
    







if __name__ == "__main__":
    app.debug = True
    app.run() 


