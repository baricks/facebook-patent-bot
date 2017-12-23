import creds
import os
import time
import urllib
from twython import Twython
from apscheduler.schedulers.blocking import BlockingScheduler
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# from PIL import Image
# from io import BytesIO
# from wand.image import Image
# from wand.color import Color

# Personalized Twitter API keys for Twython use
APP_KEY = creds.creds['CONSUMER_KEY']
APP_SECRET = creds.creds['CONSUMER_SECRET']
ACCESS_TOKEN = creds.creds['ACCESS_TOKEN']
ACCESS_SECRET = creds.creds['ACCESS_TOKEN_SECRET']

twitter = Twython(APP_KEY, APP_SECRET, ACCESS_TOKEN, ACCESS_SECRET)

# Tweets most recent Facebook patents
driver = webdriver.PhantomJS()
driver.get('http://stks.freshpatents.com/Facebook-Inc-nm1.php')

# Find element on page with posts and get element

for i in range(0,20):
    titles = driver.find_elements_by_class_name('apptitle')
    title = titles[i]
    # Get patent title
    patent_title = title.text
    # Get URL
    url = title.get_attribute('href')
    # Get patent number
    patent_number = url[43:-4]
    # Get patent PDf URL
    # pdf_link = "https://www.pat2pdf.org/patents/pat" + patent_number + ".pdf"
    # file_path = "test.pdf"
    # urllib.urlretrieve(pdf_link,file_path)
    #
    # with Image(filename="test.pdf", resolution=300) as img:
    #     with Image(width=img.width, height=img.height, background=Color("white")) as bg:
    #         bg.composite(img,0,0)
    #         bg.save(filename="image.png")

    tweet = "New US patent #" + patent_number + " from Facebook, Inc: " + patent_title + ": " + url
    print (tweet)

    # Tweet the patent
    # twitter.update_status(status=tweet, media_ids=[image_ids['media_id']])
    twitter.update_status(status=tweet)

    # Go back
    driver.get('http://stks.freshpatents.com/Facebook-Inc-nm1.php')

    # time.sleep (11000)
    time.sleep(200) #15 minutes

driver.quit()
