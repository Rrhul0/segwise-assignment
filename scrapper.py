from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

LOGIN_PAGE = 'https://www.linkedin.com/login'

def getPosts(url):
    soup = scrape(url)
    postElements = soup.find_all('li', {"class":'profile-creator-shared-feed-update__container'})
    posts=[]
    for element in postElements:
        if len(posts) ==5:
            break
        postText = element.select_one("span.break-words > span").text
        posts.append(postText)
    return posts

def scrape(url):
    driver.get(url)
    print(url)
    if driver.current_url.split("?")[0]!=url:
        login()
        if(driver.current_url.split("?")[0]!=url):
            driver.get(url)

    for _ in range(4):  # Scroll multiple times to load more posts
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Wait for new posts to load

    return BeautifulSoup(driver.page_source, 'html.parser')


def login():
    if(driver.current_url.split("?")[0]!=LOGIN_PAGE):
        driver.get(LOGIN_PAGE)

    username = driver.find_element(by='name',value="session_key")
    password = driver.find_element(by='name',value="session_password")
    username.send_keys(os.getenv("LINKEDIN_USERNAME"))
    password.send_keys(os.getenv("LINKEDIN_PASSWORD"))

    try:
        rememberMe = driver.find_element(by='name',value="rememberMeOptIn")
        rememberMe.click()
    except:
        pass

    password.send_keys(Keys.RETURN)