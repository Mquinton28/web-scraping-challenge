from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
import numpy as np

app = Flask(__name__)

def init_browser():
    executable_path = {'executable_path': '/usr/local/bin/chromedriver'}
    return Browser('chrome', **executable_path, headless=False)

def scrape():
    #Tiles
    browser = init_browser()
    mars_info = {}

    # News Urls
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)

    html = browser.html
    soup = BeautifulSoup(html, 'html.parser')

    mars_article = soup.find('div', class_='list_text')
    news_p = mars_article.find('div', class_="article_teaser_body").text
    mars_title = mars_article.find('div', class_="content_title").text
    news_ps = mars_article.find('div', class_="rollover_description").text

    mars_info["mars_article"] = mars_article
    mars_info["mars_title"] = mars_title
    mars_info["mars_paragraph"] = news_p
    mars_info["mars_paragraphs"] = news_ps
    

    # Featured Image Scrape
    url_img = ('https://www.jpl.nasa.gov/spaceimages/')
    browser.visit(url_img)
    response = browser.html
    soup_img = BeautifulSoup(response, 'html.parser')
    mars_images = soup_img.find_all('a', class_="fancybox")
    img_source = []
    for image in mars_images:
        mars_image = image['data-fancybox-href']
        img_source.append(mars_image)
    
    mars_info['url_img'] = "https://www.jpl.nasa.gov" + 


@app.route("/")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)