import sqlite3
import pandas as pd

def create_meta_db():
    # create connection to db
    connection = sqlite3.connect('meta_music.db')

    # create cursor
    cursor = connection.cursor()

    # drop tables if they exists
    cursor.execute('DROP TABLE IF EXISTS artists')
    cursor.execute('DROP TABLE IF EXISTS albums')
    cursor.execute('DROP TABLE IF EXISTS features')

    # create sql tables for artists, albums, and track features
    artist_table_schema ='''CREATE TABLE artists (
                            artist_id INTERGER PRIMARY KEY, 
                            artist TEXT NOT NULL);'''

    album_table_schema = '''CREATE TABLE albums (
                                album_id INTERGER PRIMARY KEY,
                                artist TEXT NOT NULL,
                                album TEXT NOT NULL, 
                                date TEXT NOT NULL, 
                                week_num INTEGER, 
                                meta_score INTEGER, 
                                user_score INTEGER,
                                album_img TEXT,
                                crit_rev_num INTEGER,
                                user_rev_num INTEGER,
                                record_label TEXT,
                                album_genre TEXT,
                                album_year  INTERGER,
                                artist_id INTEGER,
                            );'''

    features_table_schema = '''CREATE TABLE features(
                                feature_id INTEGER, 
                                danceability REAL, 
                                energy REAL,
                                key INTEGER, 
                                loudness REAL, 
                                mode INTEGER, 
                                speechiness REAL, 
                                acousticness REAL, 
                                instrumentalness REAL,
                                liveness REAL,
                                valence REAL, 
                                tempo REAL, 
                                duration_ms INTEGER,
                                time_signature INTEGER,
                                artist_id INTEGER,
                                album_id INTEGER,
                                FOREIGN KEY (artist_id) REFERENCES artists (artist_id),
                                FOREIGN KEY (album_id) REFERENCES albums (album_id)
                                );'''

    # create all tables
    cursor.execute(features_table_schema)
    print('table 1 created')
    cursor.execute(artist_table_schema)
    print('table 2 created')
    cursor.execute(album_table_schema)
    print('table 3 created')
    cursor.close()

def csv_to_df():
    scrape_df = pd.read('full_scrape_20yr')

def load_artists(df):
    artist_df = df['artist']
    artist_df.df.to_sql