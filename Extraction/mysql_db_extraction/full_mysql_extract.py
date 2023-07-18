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
import awswrangler as wr #info for connections to aws resources
import redshift_connector #info for aws redshift connection
import yaml
import pandas as pd

import warnings
warnings.filterwarnings('ignore')
#%% #info read text files
secrets = yaml.load(open(r'conf/secrets/creds.yaml'), Loader=yaml.FullLoader)
settings = yaml.load(open(r'conf/app/main.yaml'), Loader=yaml.FullLoader)

#%% #info connect to mysql database and query using pd
sql = open(r'conf/sql/full_mysql_extract.sql', 'r').read()
with pymysql.connect(
    host=secrets['db_dppr-book']['host'],
    user=secrets['db_dppr-book']['user'],
    password=secrets['db_dppr-book']['password'],
    db=secrets['db_dppr-book']['db'],
    port=secrets['db_dppr-book']['port']
) as conn:
    
    orders = pd.read_sql(sql, conn)



#%% #info connect to AWS
boto3.setup_default_session(
    aws_access_key_id=secrets['aws_iam_user']['access_key'],
    aws_secret_access_key=secrets['aws_iam_user']['secret_key']
)
#%% #info connect and query to AWS Redshift 
sql = open(r'conf/sql/full_redshift_extract.sql', 'r').read()
with redshift_connector.connect(
    host=secrets['aws_redshift']['host'],
    database=secrets['aws_redshift']['database'],
    port=secrets['aws_redshift']['port'],
    user=secrets['aws_redshift']['user'],
    password=secrets['aws_redshift']['password']
) as conn:
    
    orders = pd.read_sql(sql, conn)
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
# %%
