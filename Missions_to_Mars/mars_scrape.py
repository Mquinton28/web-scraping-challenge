from bs4 import BeautifulSoup
from splinter import Browser
import pymongo
import pandas as pd
import requests
from flask import Flask, render_template
import numpy as np

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
    img_url = "https://www.jpl.nasa.gov" + mars_image
    
    mars_info['url_img'] = "https://www.jpl.nasa.gov" + mars_images

    featured_img_url = img_url

    mars_info['featured_img_url'] = featured_img_url

# Mars Facts
    mars_facts_url = 'https://space-facts.com/mars/'
    browser.visit(mars_facts_url)

    mars_grab = pd.read_html(mars_facts_url)
    mars_facts = pd.DataFrame(mars_grab[0])
    mars_facts.columns = ['Mars', 'Facts']
    mars_table = mars_facts.set_index("Mars")
    mars_data = mars_table.to_html(classes='mars_data')
    mars_data = mars_data
    
    mars_info['mars_table'] = mars_data.replace('\n', ' ')

    