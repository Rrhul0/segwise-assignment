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
    # posts=["As of October 20th, the final Meta Ads campaign I had scheduled for Trieste Photo Days came to a close. Although I officially left the organization on September 13th, this campaign ran from September 20th to October 20th without any further adjustments by the current team.I crafted this campaign from the ground up, targeting specific audiences based on interests, geolocation, age groups, and utilizing advanced datasets derived from Meta Pixel and server-side Conversions API (which I had implemented over a year ago). The focus of the campaign was the 2024 Project Selection by Harry Gruyaert, the pioneer of color photography and a member of Magnum Photos.The results were remarkable: we reached 32k unique accounts with a conversion rate of 5.53%, all with a budget of only €335. What’s more, this campaign targeted highly competitive international markets, such as the US, Canada, Japan, and others, where advertising costs are significantly higher than in Italy.The effectiveness of this campaign can also be seen in the results: the 2022 Project Selection, which I was not involved with, closed with a total of 35 submitted portfolios. In 2023, my first year managing communication and advertising, we achieved 156 submitted portfolios, a 345.71% increase.This year, the 2024 edition — where I only set up the campaign — closed with 359 portfolios, marking a +130.13% increase over 2023 and an incredible +925.71% compared to 2022.Oh, and these numbers refer to actual paid submissions, as this is a pay-to-submit model, with many more portfolios uploaded but not confirmed (which also count towards engagement).Have you ever worked on a campaign that continued to deliver strong results after you stepped away? I'd love to hear your thoughts on maintaining effectiveness even when you're no longer directly involved!hashtag#DigitalMarketing hashtag#MetaAds hashtag#AdvertisingStrategy hashtag#CampaignSuccess hashtag#MarketingResults hashtag#SocialMediaMarketing hashtag#Photography hashtag#CreativeCampaigns hashtag#Targeting hashtag#MarketingGrowth hashtag#ProjectManagement",
    #     "🌞 Hello, Toronto! 🌞I'm thrilled to share that I've arrived in Toronto with my significant other, and we've been soaking up the sunny welcome! We’re taking this time to recharge and get ready for what’s next.As I settle in, I’m eagerly looking forward to the next adventure in my career. If you know of any opportunities or interesting projects, feel free to reach out—I’d love to connect and explore what the Toronto job market has to offer.", "Aloha lovely peeps,I'm moving to Toronto in October, which means I am looking for a new job there and would appreciate your support. Thank you in advance for any contacts, tips, and job offers that can help me! hashtag#OpenToWork"]
    # print(posts)
    # connectionMsg = "🚀 Great results even after you stepped away? Impressive! Curious to chat more about sustaining campaign success post-departure. Also, welcome to Toronto! Let's connect on local roles. 🌟💼"
    connectionMsg = hugginFace.getMessage(posts)
    print(connectionMsg)
    escapedProfileUrl = escape(profileUrl)
    return render_template("linkedin.html",profileUrl=escapedProfileUrl,userName="Test user",posts=posts,welcomeMsg=connectionMsg)