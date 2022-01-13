import sqlite3
import json
from basic_query_funcs import queries_dict
# func for artist queries


# print(query_artist('Twin Shadow'))
artist = 'Twin Shadow'

artist_query = queries_dict["ar_query"]("Twin Shadow")
# create context manager
with sqlite3.connect('meta_music.db') as conn:
# create cursor
    cur = conn.cursor()
# query db
    cur.execute(artist_query)
    query = cur.fetchall()
    print(json.dumps(query))
