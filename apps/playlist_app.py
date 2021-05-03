import requests
import os
import base64
import csv
import json
from datetime import datetime, date
from spotify_client import *
from config import *

def refresh_accesss_token():
    client_creds = f'{client_id}:{client_secret}'
    client_creds_b64 = base64.b64encode(client_creds.encode())

    refresh_token_header = {
        'Authorization' : f'Basic {client_creds_b64.decode()}'
    }

    # def refresh_playlist_token():
    refresh_url =  'https://accounts.spotify.com/api/token'
    refresh_params = {
        'grant_type': 'refresh_token',
        'refresh_token': f'{refresh_token}'
        
    }

    refresh_data = urlencode(refresh_params)



    r_token = requests.post(refresh_url, data=refresh_params, headers=refresh_token_header)

    refresh_response = r_token.json()

    access_token = refresh_response['access_token']

    return access_token





# def get_week_num():
playlist_token = refresh_accesss_token()
csv_path = os.path.join('..', 'data', 'test','test2.csv')
def get_week_num():
    my_date = datetime.date.today() 
    year, week_num, day_of_week = my_date.isocalendar()
    this_week = week_num
    return this_week

def get_album_tracks(album_ids):
    track_ids = []
#     request_data = json.dumps(uris)
    for album_id in album_ids:
        query = f'https://api.spotify.com/v1/albums/{album_id}/tracks'
        response = requests.get(
            query,
            headers = {
                'Content-Type': 'application/json',
                'Authorization': f'Bearer {playlist_token}'
            })
        response_json = response.json()
#         print(response_json)
        tracks = response_json['items']
        for track in tracks:
            track_ids.append(track['uri'])
    return track_ids

def search_for_albums(csv_path):
    artists=[]
    albums=[]
    albums_not_found = {'artist': [], 'album': []}
    album_ids = set()
    

#     read in weekly metaScrape csv 
    with open(csv_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
#         filter for artists and albums from current week
            if int(row['week_num'])==get_week_num():
                artists.append(row['artist'])
                albums.append(row['album'])
#   initialize spotify client
    spotify = SpotifyAPI(client_id, client_secret)
    for al, ar in zip(albums, artists):
#   search for album ids 
        temp = spotify.search({"album":al, "artist":ar}, search_type="album")
        try:
            parse_album_ids = (temp["albums"]["items"][0]["id"])
#   create dicitonary for albums not found
        except:
            albums_not_found['artist'].append(ar)
            albums_not_found['album'].append(al)
        album_ids.add(parse_album_ids)
    return(get_album_tracks(album_ids))

def add_tracks_to_playlist(playlist_id):
    track_ids = [track for track in search_for_albums(csv_path)]
    track_limit = 100 
    # using list comprehension 
    batched_tracks = [track_ids[i * track_limit:(i + 1) * track_limit] for i in range((len(track_ids) + track_limit - 1) // track_limit)]  
    url = f'https://api.spotify.com/v1/playlists/{playlist_id}/tracks'

    for batch in batched_tracks:

        request_data = json.dumps(batch)

        response = requests.post(
            url,
            data=request_data,
            headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {playlist_token}'
            })
        return(response.json())

def create_playlist():
    week_num = get_week_num()
    request_body = json.dumps({
        'name': f'2021-week {week_num} scrape',
        'description': f'metacritic rated albums for the {week_num}th of the year',
        'public': True
    })
    url = f'https://api.spotify.com/v1/users/{spotify_user_id}/playlists'


    response = requests.post(
        url,
        data = request_body,
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {playlist_token}'

    })
    response_json = response.json()
#     print(response_json)
    playlist_id = (response_json['id'])

    return add_tracks_to_playlist(playlist_id)

