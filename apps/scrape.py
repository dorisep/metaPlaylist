import json
import requests
from bs4 import BeautifulSoup
import pandas as pd
import os
import csv
from datetime import datetime
import playlist_app

def meta_scrape(week_num):
    week_num = week_num
    url_for_scrape = 'https://www.metacritic.com/browse/albums/release-date/new-releases/date'
    user_agent = {'User-agent': 'Mozilla/5.0'}
    # send response
    response_score = requests.get(url_for_scrape, headers = user_agent)
    # scrape website into variable to parse
    soup_score = BeautifulSoup(response_score.text, 'html.parser')
    
    # create temporary lists for user scores
    userP = []
    userM = []
    userN = []
    # create/initialize dictionary 
    albums_dict = {'artist':[], 'album':[], 'date':[], 'week_num':[], 'meta_score': [], 'user_score':[]}

    soup_score.find_all('td', class_='clamp-summary-wrap')
    # create soup 
    for _ in soup_score.find_all('td', class_='clamp-summary-wrap'):
        # scrape album name
        albums_dict['album'].append(_.find('a', class_= 'title').text)
        # scrape artist name and strip white space and extra characters
        albums_dict['artist'].append(_.find('div', class_='artist').text.strip().lstrip('by '))
        # scrape date
        albums_dict['date'].append(_.find('div', class_='clamp-details').find('span').text)
        # scrape meta_score, handle for changes in class name, convert data type of score to int and append to dict
        # except set to pass since all alubms have a score

        try:
            albums_dict['meta_score'].append(int(_.find('div', class_='metascore_w large release positive').text))  
        except:
            pass
        try:
            albums_dict['meta_score'].append(int(_.find('div', class_='metascore_w large release mixed').text))  
        except:
            pass 
        try:
            albums_dict['meta_score'].append(int(_.find('div', class_='metascore_w large release negative').text))  
        except:
            pass
        # scrape user score, handle errors for tbd/class name and append to temp list
        try:
            userP.append(float(_.find('div', class_='metascore_w user large release positive').text))  
        except:
            userP.append(0)
        try:
            userM.append(float(_.find('div', class_='metascore_w user large release mixed').text))  
        except:
            userM.append(0)
        try:
            userN.append(float(_.find('div', class_='metascore_w user large release negative').text))  
        except:
            userN.append(0)
            
    # merge user score by filtering scores from tbd using data type in temporary lists, convert data type of scores to int and append to dictionary        
    for a, b, c in zip(userP, userM, userN):
        if isinstance(a, float):
            albums_dict['user_score'].append(int(a * 10))
        elif isinstance(b, float):
            albums_dict['user_score'].append(int(b * 10))
        elif isinstance(c, float):
            albums_dict['user_score'].append(int(c * 10))
        else:
            albums_dict['user_score'].append(c)
# create week_num key and values for weekly scrape
    for dates in albums_dict['date']:
        albums_dict['week_num'].append((datetime.strptime(dates, '%B %d, %Y')).isocalendar()[1])
    # write dictionary to csv
    # create header
    fields = ['artist', 'album', 'date', 'week_num', 'meta_score', 'user_score'] 
    # create variable for data to be written
    data = zip(albums_dict['artist'], albums_dict['album'], albums_dict['date'], albums_dict['week_num'], albums_dict['meta_score'], albums_dict['user_score'])
    return write_csv(albums_dict, week_num)

def scrape_reviews(albums_dict, week_num):
    artists = albums_dict['artist']
    for artist in artists:
        url_for_reviews = f'https://www.metacritic.com/music/the-myth-of-the-happily-ever-after/{artist}'
        user_agent = {'User-agent': 'Mozilla/5.0'}
        # send response
        response_reviews = requests.get(url_for_reviews, headers = user_agent)
        # scrape website into variable to parse
        soup_reviews = BeautifulSoup(response_reviews.text, 'html.parser')
        # print(soup_reviews)
    playlist_app.create_playlist(week_num)
    return albums_dict


def write_csv(albums_dict, week_num):
    # write dictionary to csv
    # csv variables
    output_path = os.path.join('..', 'data', 'meta_scrape.csv')
    # create header
    fields = ['artist', 'album', 'date', 'week_num', 'meta_score', 'user_score'] 
    # create variable for data to be written
    data = zip(
            albums_dict['artist'], 
            albums_dict['album'], 
            albums_dict['date'], 
            albums_dict['week_num'], 
            albums_dict['meta_score'], 
            albums_dict['user_score']
            )
    with open(output_path, 'a') as csvfile:
        writer = csv.writer(csvfile)
        for d in data:
            writer.writerow(d)
    return playlist_app.create_playlist(week_num)
