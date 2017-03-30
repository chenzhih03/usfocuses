from urllib import urlencode
import requests
import time
import random
import urllib
import math

base_url = 'https://www.congress.gov/search?'
search = 'q='+'{"source":"legislation","congress":'+'"114"'+',"subject":'+'"Health"'+'}'
pagesize = 250
"""
   The function below scrapes all the urls for one subject of one congress number.This function can be
   called in a for loop of all the subjects and congress nubmers to obtain all the meta data. MongoDB can be
   used to store the metadata. And mongoexport is used to export the data as a jason file for further scraping.
"""

def scrape_legislation(sub_name,congress_num):

    url_list = []
    date_list = []
    name_list = []
    params1 = OrderedDict([('pageSize','250'),('page','1')])
    search1 = search.replace('Health',sub_name)
    search2 = search1.replace('114',congress_num)
    base_url1 = base_url + search2
    result = requests.get(base_url1,params = urlencode(params1))
    if result.status_code == 200:

        soup = BeautifulSoup(result.content,'lxml')

        links = soup.find_all('span',{'class':'result-heading'})

        result_item = soup.find_all('span',attrs={'class':'result-item'})
        # number of bills in this subject
        num_bill = int(soup.find('span',{'class':'results-number'}).text.split()[-1].replace(',',''))
        num_pages = int(math.ceil(float(num_bill)/250))

        if num_pages == 1:
            for link_num in range(0,len(links),2):
                name_list.append(links[link_num].text)
                url_list.append(links[link_num].find('a').get('href').replace('?r=','/text?r='))
            for i in range(len(result_item)):
                text_sp = result_item[i].text.split()
                if text_sp[0]=='Latest':
                    date_list.append(text_sp[2])

        else:
            for link_num in range(0,len(links),2):
                name_list.append(links[link_num].text)
                url_list.append(links[link_num].find('a').get('href').replace('?r=','/text?r='))
            for i in range(len(result_item)):
                text_sp = result_item[i].text.split()
                if text_sp[0]=='Latest':
                    date_list.append(text_sp[2])
            for page_num in range(2,num_pages+1):
                params_p = OrderedDict([('pageSize','250'),('page',str(page_num))])
                result_p = requests.get(base_url1, params = urlencode(params_p))

                if result_p.status_code == 200:

                    soup_p = BeautifulSoup(result_p.content,'lxml')
                    links_p = soup_p.find_all('span',{'class':'result-heading'})
                    result_item_p = soup_p.find_all('span',attrs={'class':'result-item'})

                    for link_num in range(0,len(links_p),2):
                        name_list.append(links_p[link_num].text)
                        url_list.append(links_p[link_num].find('a').get('href').replace('?r=','/text?r='))

                    for i in range(len(result_item_p)):
                        text_sp_p = result_item_p[i].text.split()
                        if text_sp_p[0]=='Latest':
                            date_list.append(text_sp_p[2])


        return {'subject':sub_name,'congress':congress_num,'links':url_list,'dates':date_list[0::2],'name':name_list}
