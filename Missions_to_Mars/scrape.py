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
    mars_titles = {}

    # News Urls
    url = 'https://mars.nasa.gov/news/'
    browser.visit(url)
    time.sleep(2)

    html = browser.mars_html
    soup = BeautifulSoup(html, 'html.parser')

    mars_titles['news_title'] = soup.find('div', class_="content_title").get_text()
    mars_titles["news_snip"] = soup.find('div', class_="rollover_description_inner").get_text()