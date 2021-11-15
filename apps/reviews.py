import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path
import re

###
# pickle import for large dataframes
###
#import pickle

###
# a python file that takes a csv file that has scraped data from metacritics aggragting site
# for albums and builds urls to scrape specific data for album images, number of critic and 
# user reviews, record labels and genre of the albums
###
def load_csv():
    # import csv file and make a dataframe
    file_path = Path('..', 'data', 'historical_data',  'combined_csv.csv')
    df = pd.read_csv(file_path)
    return(df)

###
# a very specific case that I need to address but is here in case it is encoutered again 
###
# scrape_df.loc[scrape_df.index[641], 'album'] = '#N/A'

def create_review_url(df):
###
# takes a df latest metascrape, cleans the artist and album strings
# and adds a new column of urls to scrape review values
# some language to a handle any disconnects or timeouts if 
# running dataframes with more than 400 rows.
###

# a list for creating pickles if needed
#     pickles = []
    review_urls = []
    # iterate over dataframe
    for i, j in df.iterrows():
    #     clean album and artist names of all nonalpha except for ! and accent marks
        al = re.sub(r'[^-A-Za-z0-9!áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]+', '', j['album'])
        ar = re.sub(r'[^-A-Za-z0-9!áéíóúÁÉÍÓÚâêîôÂÊÎÔãõÃÕçÇ ]+', '', j['artist'])
    # correct instances of multilple spaces
        al = re.sub(' +', ' ', al)
        ar = re.sub(' +', ' ', ar)
    # make lowercase and join words with - for url
        url_end = f'{al}/{ar}'.replace(" ", "-").lower() 
    # concat url for review scrape    
        url_beginning ='https://www.metacritic.com/music/'
        review_urls.append(url_beginning + url_end)
        pickles.append(al+'-'+ar)
# get value of colmuns to use for new column position
    new_col_position = len(df.columns)
# Use insert to add review_urls column and values to dataframe
    df.insert(new_col_position, "review_urls", review_urls)
    df.insert(new_col_position, 'pickle_name', pickles)
    return df

def scrape_reviews(df):
    ###
    # takes a meta_scrape dataframe with review urls added
    # and scrapes the num of reviews-both critics and users-
    # album image, record label and first listed genre of 
    # album and returns a dataframe
    ###
#     lists for collecting scraped data
    img = []
    crit_num = []
    user_num = []
    label = []
    genre = []
    
### 
# set total rows and count variable 
# df_total = df['album'].count
# count = 0   
# iterate over dataframe of scraped aggragate album rating from metacritic
# for scraping review data for each album
###
    for i, j in df.iterrows():
###
# following section sets up for loop to create a pickle file for each album scrape
# in case of dicsonnect or connection time out. checks for pickle files and picks
# up from last created file.
###
#         added to coundter
#         count+=1
# #         check for file in pickle if none then continue   
#         if Path('../data/pickle/'+j['pickle_name']+'.pickle').is_file():
#             # file exists
#             print('Pity the fool who finds my file')
#             with open('../data/pickle/'+j['pickle_name']+'.pickle', 'rb') as handle:
#                 b = pickle.load(handle)
#                 img.append(b['img'])
#                 crit_num.append(b['crit_num'])
#                 user_num.append(b['user_num'])
#                 label.append(b['label'])
#                 genre.append(b['genre'])
                
#             continue
###
# beginning of scrape of review page for each album
###
        url = j['review_urls']
        user_agent = {'User-agent': 'Mozilla/5.0'}
        # send response
        response_reviews = requests.get(url, headers = user_agent)
        # scrape website into variable to parse
        soup_reviews = BeautifulSoup(response_reviews.text, 'html.parser')
        ########### comment back in from here
        # scrape album image 
        try:
            img_soup = soup_reviews.find('meta', property="og:image")
            img.append(img_soup['content'])
        except:
            img.append(None)
        # scrape num of critical reviews
        try:
            num_rev=(soup_reviews.find('span', itemprop="reviewCount"))
            crit_num.append(num_rev.text.strip())
        except:
            crit_num.append(None)
        # scrape num of user reviews
        if j['user_score'] == 0:
            user_num.append(0)
        else:
            try:
                user_revs = float(soup_reviews.find('div', class_='metascore_w user large album positive').text)
                user_num.append(int(user_revs*10))
            except:
                pass
            try:
                user_revs = float(soup_reviews.find('div', class_='metascore_w user large album mixed').text)
                user_num.append(int(user_revs*10))
            except:
                pass
            try:
                user_revs = float(soup_reviews.find('div', class_='metascore_w user large album negative').text)
                user_num.append(int(user_revs*10))
                countneg+=1
            except:
                pass
        # scrape record labels
        try:
            label_class = soup_reviews.find_all("span", itemprop="name")
            label.append(label_class[2].text.strip())
        except:
            label.append(None)
        # scrape genre
        try:
            genre.append(soup_reviews.find("span", itemprop="genre").text)
        except:
            genre.append(None)
###
# create pickle here for each album if needed with counter  
###
#         a = {
#             'img': img[-1],
#             'crit_num': crit_num[-1],
#             'user_num': user_num[-1],
#             'label': label[-1],
#             'genre': genre[-1] 
#         }
        
#         with open('../data/pickle/'+j['pickle_name']+'.pickle', 'wb') as handle:
#             pickle.dump(a, handle)
#         print(j['artist'])
#         print(f'{count} of {df_total} run')
      
     
       
    # drop column for url and add scrapped lists to dataframe
    df = df.drop(columns='review_urls').assign(album_img = img, crit_rev_num = crit_num, user_rev_num = user_num, record_label = label, album_genre = genre)
    return df

df = load_csv()
full_scrape_df = scrape_reviews(create_review_url(df))

full_scrape_df.to_csv('full_scrape_20yr' ,index=False)
###
# code snippet for removing pickle files after completed run
###

# pickle_path = Path('../data/pickle/')

# pickle_files = pickle_path.glob('*.pickle')

# for pickle in pickle_files:
#     pickle.unlink()
