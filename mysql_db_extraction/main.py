#%% #info steps
    # step read text files
    # step connect to mysql database and query 
    # step write to AmazonS3 bucket 
    # step connect to AmazonS3 bucket
    # step write to AmazonS3 bucket
    # steps list object in AmazonS3 bucket
    # step code to delete object from AmazonS3 bucket


#%% #info library imports
import pymysql
import csv
import boto3
import awswrangler as wr
import yaml
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
#%% #info read text files
sql = open(r'conf/sql/extract.sql', 'r').read()
secrets = yaml.load(open(r'conf/secrets/creds.yaml'), Loader=yaml.FullLoader)
settings = yaml.load(open(r'conf/app/main.yaml'), Loader=yaml.FullLoader)

#%% #info cconnect to mysql database and query using pd
with pymysql.connect(
    host=secrets['db_dppr-book']['host'],
    user=secrets['db_dppr-book']['user'],
    password=secrets['db_dppr-book']['password'],
    db=secrets['db_dppr-book']['db'],
    port=secrets['db_dppr-book']['port']
) as conn:
    
    orders = pd.read_sql(sql, conn)

#%% #info connect to AmazonS3 bucket
boto3.setup_default_session(
    aws_access_key_id=secrets['aws']['access_key'],
    aws_secret_access_key=secrets['aws']['secret_key']
)
#%% #info write df to AmazonS3 bucket as parquet file
wr.s3.to_parquet(
    df=orders,
    path=f's3://{settings["aws_bucket"]["bucket_name"]}/{settings["aws_bucket"]["object_key"]}'
)
#%% #info list object in AmazonS3 bucket
print(wr.s3.list_objects(f's3://{settings["aws_bucket"]["bucket_name"]}/'))
#%% #info delete object from AmazonS3 bucket
wr.s3.delete_objects(
    path=f's3://{settings["aws_bucket"]["bucket_name"]}/{settings["aws_bucket"]["object_key"]}'
)