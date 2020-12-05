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
    