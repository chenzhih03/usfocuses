from selenium import webdriver
from urllib import urlencode
import time
import random
from bs4 import BeautifulSoup
#browser = webdriver.Firefox()
import requests

base_url = 'https://millercenter.org/'

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

with open('speech.dat','w') as f:
    f.write(str(speech_list))
    f.write(str(date_list))
    f.write(str(links_list))
