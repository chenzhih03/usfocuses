from selenium import webdriver
from urllib import urlencode
import time
import random
from bs4 import BeautifulSoup
#browser = webdriver.Firefox()
import requests
from pymongo import MongoClient

# Define the MongoDB database and table
db_cilent = MongoClient()
db = db_cilent['presidential']
table = db['meta']

base_url = 'https://millercenter.org'

#'''
#Scroll down the website so all the content can be shown
#'''

url_speech = 'https://millercenter.org/the-presidency/presidential-speeches'

browser = webdriver.Firefox()

browser.get(url_speech)

i=0
while i<100:
    i = i + 1
    browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(3)

speech_content = browser.page_source

soup = BeautifulSoup(speech_content,'lxml')

all_links_name = soup.find_all('div',{'class':'views-row'})

links_list = []
speech_list = []
date_list = []
for each_speech in all_links_name:
    link = base_url + each_speech.find('a').get('href')
    text = each_speech.find('a').text.split(':')
    date = text[0]
    speech = text[1]
    links_list.append(link)
    speech_list.append(speech)
    date_list.append(date)

for i in range(971,len(links_list)):
    browser.get(links_list[i])
    trans1 = BeautifulSoup(browser.page_source,'lxml').find('div',{'class':'transcript-inner'})

    if trans1:
        text = trans1.text.replace('Transcript','').replace('\n','')
    else:
        trans2 = BeautifulSoup(browser.page_source,'lxml').find('div',{'class':'view-transcript'})
        text = trans2.text.replace('Transcript','').replace('\n','')

    table.insert_one({'date':date_list[i],'speech_title':speech_list[i],'link':links_list[i],'content':text})
