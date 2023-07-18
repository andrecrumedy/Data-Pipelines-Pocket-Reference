#%% #INFO STEPS
    # step read text files
    # step connect to mysql database and query 
    # step write to AmazonS3 bucket 
    # step connect to AmazonS3 bucket
    # step write to AmazonS3 bucket
    # steps list object in AmazonS3 bucket
    # step code to delete object from AmazonS3 bucket


#%% #INFO LIBRARY IMPORTS
import pymysql
import csv
import boto3
import awswrangler as wr #info for connections to aws resources
import redshift_connector #info for aws redshift connection
import yaml
import pandas as pd

import warnings
warnings.filterwarnings('ignore')

#%% #INFO RE-USABLE FUNCTIONS
    
    #INFO WRITE DF TO AWS S3 BUCKET AS PARQUET FILE
def df_to_s3_bucket(df:pd.DataFrame, bucket_folder:str, file_name:str):
    ''' 
    aws session must be defined in using boto3  

    uses awswragular to save file to s3 bucket
    '''
    wr.s3.to_parquet(
        df=df,
        path=f's3://{bucket_folder}/{file_name}'
    )


#%% #INFO READ IN TEXT FILES
secrets = yaml.load(open(r'conf/secrets/creds.yaml'), Loader=yaml.FullLoader)
settings = yaml.load(open(r'conf/app/main.yaml'), Loader=yaml.FullLoader)

#%% #INFO CONNECT TO AWS
boto3.setup_default_session(
    aws_access_key_id=secrets['aws_iam_user']['access_key'],
    aws_secret_access_key=secrets['aws_iam_user']['secret_key']
)

#%% #INFO PIPELINE: FULL EXTRACTION FROM MYSQL TO S3 BUCKET 

    # info read in query from application text file
sql = open(r'conf/sql/mysql_full_extract.sql', 'r').read()

    #info connect and query full dataset from mysql database
with pymysql.connect(
    host=secrets['db_dppr-book']['host'],
    user=secrets['db_dppr-book']['user'],
    password=secrets['db_dppr-book']['password'],
    db=secrets['db_dppr-book']['db'],
    port=secrets['db_dppr-book']['port']
) as conn:
    
    orders = pd.read_sql(sql, conn)

    #info load dataframe into AWS s3 bucket
df_to_s3_bucket(df=orders, 
                bucket_folder=settings['aws_bucket']['bucket_name'],
                file_name=settings['aws_bucket']['file_names']['mysql_full_extract'])


#%% #INFO PIPELINE: FULL EXTRACTION FROM REDSHIFT TO S3 BUCKET
    
    # info read in query from application text file
sql = open(r'conf/sql/redshift_full_extract.sql', 'r').read()

    #info connect and query full dataset from Redshift database
with redshift_connector.connect(
    host=secrets['aws_redshift']['host'],
    database=secrets['aws_redshift']['database'],
    port=secrets['aws_redshift']['port'],
    user=secrets['aws_redshift']['user'],
    password=secrets['aws_redshift']['password']
) as conn:
    
    orders = pd.read_sql(sql=sql, con=conn)

    #info load dataframe into AWS s3 bucket
df_to_s3_bucket(df=orders, 
                bucket_folder=settings['aws_bucket']['bucket_name'],
                file_name=settings['aws_bucket']['file_names']['redshift_full_extract'])

#%% #INFO PIPELINE: INCREMENTAL EXTRACTION FROM REDSHIFT TO S3 BUCKET

    #info read in redshift query for lastupdated timestamp
sql = open(r'conf/sql/redshift_last_updated.sql', 'r').read()

    # info connect and query dwg(redshift) for last updated timestamp
with redshift_connector.connect(
    host=secrets['aws_redshift']['host'],
    database=secrets['aws_redshift']['database'],
    port=secrets['aws_redshift']['port'],
    user=secrets['aws_redshift']['user'],
    password=secrets['aws_redshift']['password']
) as conn:
    
    last_updated = str(pd.read_sql(sql=sql, con=conn).iloc[0,0])
    # info read in mysql query
sql = open(r'conf/sql/mysql_incremental_extract.sql', 'r').read()
    
    #info connect and query incremental dataset from mysql database
with pymysql.connect(
    host=secrets['db_dppr-book']['host'],
    user=secrets['db_dppr-book']['user'],
    password=secrets['db_dppr-book']['password'],
    db=secrets['db_dppr-book']['db'],
    port=secrets['db_dppr-book']['port']
) as conn:
    orders = pd.read_sql(sql=sql, con=conn, params=last_updated)

    #info load dataframe into AWS s3 bucket
df_to_s3_bucket(df=orders, 
                bucket_folder=settings['aws_bucket']['bucket_name'],
                file_name=settings['aws_bucket']['file_names']['redshift_incremental_extract'])

# #INFO CONNECT AND QUERY AWS REDSHIFT FOR LAST UPDATED

#%% #INFO LIST ALL OBJECTS IN AWS S3 BUCKET
print(wr.s3.list_objects(f's3://{settings["aws_bucket"]["bucket_name"]}/'))
#%% #INFO DELETE OBJECT FROM AWS S3 BUCKET
wr.s3.delete_objects(
    path=f's3://{settings["aws_bucket"]["bucket_name"]}/{settings["aws_bucket"]["object_key"]}'
)
# %%
