import numpy as np
import pandas as pd





df = pd.read_json('congress_meta_final_test.json')





new_df = pd.DataFrame(columns=df.columns)

for i in range(2):#df.shape[0]):
    sub_row = df.iloc[i,:]
    num_links = len(sub_row['links'])
    print num_links
    for j in range(num_links):
        row = pd.DataFrame([[sub_row['_id'],sub_row['congress'],sub_row['dates'][j].encode('utf-8'),sub_row['links'][j].encode('utf-8'),sub_row['name'][j].encode('utf-8'),sub_row['subject'].encode('utf-8')]],columns=df.columns)
        new_df = new_df.append(row)
	print new_df.shape

new_df.to_csv('congress_meta.csv')
