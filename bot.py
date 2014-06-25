#! /bin/python

import re
import datetime

import pymongo
from pymongo import MongoClient
import requests
from bs4 import BeautifulSoup

REGEX = r'About (.*) results'
keywords = ['Arvind Kejriwal', 'Narendra Modi', 'Rahul Gandhi', 'Sonia Gandhi', 'BJP', 'AAP', 'Congress India']

def number_of_search_results(key):
    def extract_results_stat(url):
        headers = { 
            'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:12.0) Gecko/20100101 Firefox/21.0'
        }
        search_results = requests.get(url, headers=headers, allow_redirects=True)
        soup = BeautifulSoup(search_results.text)
        result_stats = soup.find(id='resultStats')
        m = re.match(REGEX, result_stats.text)
        return int(m.group(1).replace(',',''))

    google_main_url = 'https://www.google.co.in/search?q=' + key
    google_news_url = 'https://www.google.co.in/search?hl=en&gl=in&tbm=nws&authuser=0&q=' + key
    return (extract_results_stat(google_main_url), extract_results_stat(google_news_url))

if __name__ == '__main__':
    conn = MongoClient()
    db = conn['search_results']
    current_time = datetime.datetime.utcnow()
    for key in keywords:
        google_main, google_news = number_of_search_results(key) 
        db.search_results.insert({'time': current_time, 'name': key, 'google_main': google_main, 'google_news': google_news})