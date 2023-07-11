# Data Pipeines Pocket Reference: Moving and Processing Data for Analytics  
Repo is updated daily as I work through all examples in this book. Repo structure is subjet to change.

This repo for the code walkthroughs of this book and a place for me to showcase my Data Engineering skills with AWS and other Products. These examples will differ from the book such that I use best practice(based on experience or research) python libraires and techniques. Please see 'notes' section each python module's readme file for descriptions on the differences. It's organized with the same flow as the book: Extraction, Loading, Transformations, and Pipeline Orchestration. 

## `Environments: Python, AWS, MY SQL, Amazon Redshift`

> Python Set-up

1. using virtual env to isolate packages  
1. installing boto3 as connection library to Amazon s3  

> AWS Account and AWS S3 Set-up  

1. Setting and Amazon accoutn with 12 months free trial
1. Creating Amazon S3 bucket(storage account) using default settings
1. creating a IAM(Identity Access Management) from the console management and add "AmazonS3FullAccess" policy to the permission and getting access key, secret key, and account ID for the application to authenticate and access S3 bucket

> MySQL Instance Set-up  

- Although MySQL can be installed on local machine or VM for free, it is more straightforward to utilize Amazon RDS to create an DB instance of MySQL folliwing  <a href="https://aws.amazon.com/getting-started/hands-on/create-mysql-db/" target="_blank">these instuctions.</a>


## `Project Set-up`  

>Application Structure  
- /env: virtual environment folder *(not uploaded to git)*  
- /mysql_data_setup: python module for MySQL table creation  
- /mysql_db_extraction: python module for MySQL --> AmazonS3 bucket
- __init__.py: to be recognized as python package
- .gitignore: definition of files/folders not uploaded to repo

> Interactions with MySQL instance  

- options for connecting to MySQL Database:  
MySQL command-line client, MySQL Workbench, or pymysql python library

## `Project Run-Steps`  
1. Configure Environments
1. Run 'main.py' in /mysql_data_setup to load data in MySQL database
1. Use MySQL Workbench to verify table creation in MySQL database.
1. Run 'full_mysql_extract.py in /mysql_db_extraction to pipeline data from MySQL database to AmazonS3 bucket.
1. Verify file in AmazonS3 bucket programitaclly or the AmazonS3 console
1. Run 'main.py' in /redshift_data_setup to load data in MySQL database
1. Run 'main.py in /redshift_db_extraction to pipeline data from Amazon Redshit data warehouse to AmazonS3 bucket.
