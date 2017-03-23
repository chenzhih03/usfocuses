n=20
csv_files=[]
for i in range(1,n):
    csv_files.append('df_congress{}_change.csv'.format(i))
df_full = spark.read.csv('s3a://usfocus/congress_full.csv',header = True,inferSchema=True,sep=",")
 for csv_file in csv_files:
     base_url = 's3a://usfocus/'
     link = base_url + csv_file
     df_one = spark.read.csv(link,header = True,inferSchema=True,sep=",")
     df_full = df_full.union(df_one)

df_full.count()


df_data = df_full.select('content', 'subject','dates','name','congress')

df_clean = df_data.filter(df_data['content']!='NA')

df_clean.write.format('com.databricks.spark.csv').options(header='true').save('s3a://usfocus/congress_full.csv')
