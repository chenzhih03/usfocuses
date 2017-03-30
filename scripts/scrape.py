from bs4 import BeautifulSoup
import requests
import pandas as pd
import boto3

s3 = boto3.client("s3")
df = pd.read_csv('congress_meta.csv')
row_num = df.shape[0]
stop_nums = range(0,row_num,int(row_num)/10)[0:-1]
stop_nums.append(row_num)

"""
This function divide the all the docs needs to be scraped into 10 parts.
Files(csv format) are saved in the s3 bucket.
"""
for i in range(len(stop_nums)-1):
    start_point = stop_nums[i]
    stop_point = stop_nums[i+1]
    new_df = df.iloc[start_point:stop_point,:]
    df_content = pd.DataFrame(columns = ['content'])
    for link in new_df['links'].values:
        r = requests.get(link)
        if r.status_code == 200:
            soup = BeautifulSoup(r.content,'lxml')
            text_string = soup.find_all('pre',{'id':'billTextContainer'})[0].text.encode('utf-8')
            df_column = pd.DataFrame([[text_string]],columns=['content'])
            df_content = df_content.append(df_column)

    df_content.to_csv('links{}.csv'.format(i))
    s3.upload_file('links{}.csv'.format(i),'usfocus','links{}.csv'.format(i))
    new_df['content'] = df_content.values
    new_df.to_csv('df_congress{}.csv'.format(i))
    s3.upload_file('df_congress{}.csv'.format(i),'usfocus','df_congress{}.csv'.format(i))
