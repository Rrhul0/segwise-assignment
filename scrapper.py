import requests
from bs4 import BeautifulSoup
import os

def getPosts(url):
    soup = scrape(url)
    print(soup.prettify())
    return soup.find_all('li', {"class":'profile-creator-shared-feed-update__container'})

def scrape(url='https://www.example.com'):
    client = login()
    response = client.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    return soup


def login():
    LOGIN_PAGE = 'https://www.linkedin.com/login'
    LOGIN_URL= 'https://www.linkedin.com/checkpoint/lg/login-submit'
    client = requests.Session()
    #get url, soup object and csrf token value
    html = client.get(LOGIN_PAGE).content
    soup = BeautifulSoup(html, "html.parser")
    csrf = soup.find('input', dict(name='loginCsrfParam'))['value']
    #create login parameters
    login_information = {
        'session_key':os.getenv("LINKEDIN_USERNAME"),
        'session_password':os.getenv("LINKEDIN_PASSWORD"),
        'loginCsrfParam': csrf,
    }

    #try and login
    try:
        client.post(LOGIN_URL, data=login_information)
        print("Login Successful")
        return client
    except:
        print("Failed to Login")