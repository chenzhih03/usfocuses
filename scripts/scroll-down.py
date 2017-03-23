#import selenium and time to allow browse the webs and delay
from selenium import webdriver
import time

#Open a Firefox browser

browser = webdriver.Firefox()

def scroll_down(url, scroll_times = 100, sleep_time = 3):
#'''
#Scroll down the website so all the content can be shown
#'''
# depend on the waiting time each refresh takes and number of refreshes you need,
# adjust your waiting time and number of refreshes
    num_refreshes = 100
    wait_time = 3
    while i <= num_refreshes:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(wait_time)

if (__name__ == '__main()__'):
    scroll_down(url, scroll_times = 100, sleep_time = 3):
