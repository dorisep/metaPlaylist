import wikipedia
import csv
import os

csv_path = os.path.join('..', 'data', 'test', 'test2.csv')
search = []
disc_dict = {}
with open(csv_path, newline='', encoding = "ISO-8859-1") as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        # print(row)
#         filter for artists and albums from current week
        if int(row['week_num']) == 28:
            artist = (row['artist'])
            search = wikipedia.search(f'{artist} discography')
            if f'{artist} discography' in search:
                print(True)
            else:
                print(False)
            # disc_dict[artist] = 
           
            # if row["artist"] in :
            #     print(f'{row["artist"]} has discography')
# for a in disc_dict.values():
#     print(a)
