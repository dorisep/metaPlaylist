import sqlite3
import json

# def query_artist(artist):
#     command = ("select * from albums where artist = ?;", [artist])
#     return command

# print(query_artist('Twin Shadow'))
artist = 'Twin Shadow'
# queries_dict = {"ar_query": query_artist}
# test = queries_dict["ar_query"]("Twin Shadow")
# create context manager
command = (f"select * from albums where artist = '{artist}'")

with sqlite3.connect('meta_music.db') as conn:
# create cursor
    cur = conn.cursor()
# query db
    cur.execute(command)
    query = cur.fetchall()
    print(json.dumps(query))
