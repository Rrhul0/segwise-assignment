from flask import Flask
from flask import render_template
from flask import request
import scrapper
import hugginFace
from dotenv import load_dotenv
# to show user provided value (html injection)
from markupsafe import escape

load_dotenv()

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("index.html")

@app.route("/linkedin/")
def linkedinProfile():
    profileUrl = request.args.get("profileUrl")
    # check if profileUrl is valid
    if(profileUrl is None):
        return "No profile URL provided"
    elif (profileUrl == ""):
        return "Empty profile URL provided"
    elif (profileUrl.find("linkedin.com/in/") == -1):
        return "Invalid profile URL"
    elif (profileUrl.find("https://") == -1):
        profileUrl = "https://"+profileUrl
    
    details = scrapper.getProfileDetails(profileUrl)
    posts = scrapper.getPosts(profileUrl)
    connectionMsg = hugginFace.getMessage(details,posts)
    escapedProfileUrl = escape(profileUrl)
    return render_template("linkedin.html",profileUrl=escapedProfileUrl,userName="Test user",posts=posts,welcomeMsg=connectionMsg,details=details)