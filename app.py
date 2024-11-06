from flask import Flask
from flask import render_template
from flask import request
import scrapper
import hugginFace
from dotenv import load_dotenv
import os

load_dotenv()

# to show user provided value (html injection)
from markupsafe import escape

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/linkedin/")
def linkedinProfile():
    profileUrl = request.args.get("profileUrl")
    posts = scrapper.getPosts(profileUrl+"/recent-activity/all")
    connectionMsg = hugginFace.getMessage(posts)
    print(connectionMsg)
    escapedProfileUrl = escape(profileUrl)
    return render_template("linkedin.html",profileUrl=escapedProfileUrl,userName="Test user",posts=posts)