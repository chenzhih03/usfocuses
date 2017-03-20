from selenium import webdriver
import time

#Open a Firefox browser

browser = webdriver.Firefox()

def scroll_down(url, scroll_times = 100, sleep_time = 3):
#'''
#Scroll down the website so all the content can be shown
#'''
    while i <= 100:
        browser.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(3)

if (__name__ == '__main()__'):
    scroll_down(url, scroll_times = 100, sleep_time = 3):
