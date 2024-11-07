from bs4 import BeautifulSoup
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from typing import List
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=chrome_options)

LOGIN_PAGE = 'https://www.linkedin.com/login/'

def getPosts(url):
    print('getting posts')
    if (url[-1] != "/"):
        url = url + "/"
    soup = scrape(url+"recent-activity/all/")
    postElements = soup.find_all('li', {"class":'profile-creator-shared-feed-update__container'})
    posts=[]
    for element in postElements:
        if len(posts) == 5:
            break
        postText = element.select_one("span.break-words > span").text
        posts.append(postText)
    return posts

def scrape(url):
    driver.get(url)
    print(url)
    print("scrap")
    print(driver.current_url)
    if driver.current_url.split("?")[0]!=url or driver.get_cookie('li_at') is None:
        login()
        if(driver.current_url.split("?")[0]!=url):
            driver.get(url)

    for _ in range(4):  # Scroll multiple times to load more posts
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.PAGE_DOWN)
        time.sleep(1)  # Wait for new posts to load

    return BeautifulSoup(driver.page_source, 'html.parser')

def getProfileDetails(url):
    print("getting profile details")
    soup = scrape(url)
    detailSections:List[BeautifulSoup] = soup.find_all('section', {"class":'artdeco-card'})
    details = {}
    for section in detailSections:
        # get name of the user profile
        if not section.find('div', class_='pv-profile-card__anchor'):
            titleElment = section.find('h1')
            title = titleElment.get_text(strip=True) if titleElment else None
            if title:
                details['name'] = title

        # get about text
        if section.find('div', id='about', class_='pv-profile-card__anchor'):
            about_div = section.find('div', class_='inline-show-more-text--is-collapsed')
            about_span = about_div.find('span', {'aria-hidden': 'true'})
            about_text = about_span.get_text(strip=True) if about_span else None
            if about_text:
                details['about'] = about_text

        # get experiences of user
        elif section.find('div', id='experience',class_='pv-profile-card__anchor'):
            experiences = []
            for li in section.select('ul > li.artdeco-list__item'):
                try:
                    experience = {}
                    # Job title
                    job_title = li.select_one('div.mr1.t-bold span[aria-hidden="true"]')
                    experience['job_title'] = job_title.get_text(strip=True) if job_title else None

                    # Company name
                    company_name = li.select_one('span.t-14.t-normal span[aria-hidden="true"]')
                    experience['company_name'] = company_name.get_text(strip=True) if company_name else None

                    # Employment duration
                    duration = li.select_one('span.t-black--light span.pvs-entity__caption-wrapper')
                    experience['duration'] = duration.get_text(strip=True) if duration else None

                    # Location
                    location = li.select('span.t-14.t-black--light span[aria-hidden="true"]')
                    experience['location'] = location[-1].get_text(strip=True) if location else None

                    experiences.append(experience)
                except:
                    pass
            details['experiences'] = experiences
        
    return details

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