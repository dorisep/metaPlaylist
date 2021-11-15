import json
import sqlite3

with sqlite3.connect('test.db') as conn:
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM mytable WHERE column=?;", [key])
    data = cursor.fetchall()
    json.dumps(data)



# def get_my_jsonified_data(key):
#     with sqlite3.connect('test.db') as conn:
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM mytable WHERE column=?;", [key])
#         data = cursor.fetchall()
#         return json.dumps(data)