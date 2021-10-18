import schedule
import time
from meta_scrape import metaScorePages

# variables for scrape

def job():
    print(time.localtime(time.time()))
    metaScorePages(41)
# schedule.every(10).minutes.do(print('meh'))

schedule.every(1).minutes.do(job)
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
schedule.every().friday.do(job)
# schedule.every().wednesday.at("13:15").do(job)
# schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)