import wikipedia
import csv
import os

csv_path = os.path.join('..', 'data', 'test', 'test2.csv')


with open(csv_path, newline='', encoding = "ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
#         filter for artists and albums from current week
        if int(row['week_num'])==28:
            print(row['artist'])
            # print(wikipedia.search(row['album']))
        