from more_itertools import unique_everseen
with open('meta_scrape.csv','r') as f, open('clean_meta_scrape.csv','w') as out_file:
    out_file.writelines(unique_everseen(f))