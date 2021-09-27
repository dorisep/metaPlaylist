import sqlite3

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
                        name TEXT NOT NULL);'''

album_table_schema = '''CREATE TABLE albums (
                            album_id INTERGER PRIMARY KEY, 
                            album TEXT NOT NULL, 
                            date TEXT NOT NULL, 
                            week_num INTEGER, 
                            meta_score INTEGER, 
                            user_score INTEGER,
                            artist_id INTEGER,
                            FOREIGN KEY(artist_id) REFERENCES artist (artist_id)
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

cursor.execute(artist_table_schema)

cursor.execute(album_table_schema)


#check for tables 
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
tables = cursor.fetchall()
print(tables)