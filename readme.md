# Data Pipeines Pocket Reference: Moving and Processing Data for Analytics

## `Environments: Python, AWS, MY SQL, Amazon Redshift`

> Python Set-up

1. using virtual env to isolate packages  
1. installing boto3 as connection library to Amazon s3  

> AWS Account and AWS S3 Set-up  

1. Setting and Amazon accoutn with 12 months free trial
1. Creating Amazon S3 bucket(storage account) using default settings
1. creating a IAM(Identity Access Management) from the console management and add "AmazonS3FullAccess" policy to the permission and getting access key, secret key, and account ID for the application to authneticate and access S3 bucket

> MySQL Instance Set-up  

- Although MySQL can be installed on local machine or VM for free, it is more straightforward to utilize Amazon RDS to create an DB instance of MySQL folliwing  <a href="https://aws.amazon.com/getting-started/hands-on/create-mysql-db/" target="_blank">these instuctions.</a>


## `Project Set-up`  

>Application Structure  
- /env: virtual environment folder *(not uploaded to git)*  
- /mysql_data_setup: python module for MySQL table creation  
- /mysql_db_extraction: python module for MySQL --> AmazonS3 bucket
    - /conf:: config files for application
    - main.py: main extraction pipeline code  
- /secret: connection secrets *(not uploaded to git)*

> Interactions with MySQL instance  

- options for connecting to MySQL Database:  
MySQL command-line client, MySQL Workbench, or pymysql python library

## `Project Run-Steps`  
1. Configure Environments
1. Run 'main.py' in /mysql_data_setup to load data in MySQL database
1. Use MySQl Workbench to verify table creation in MySQL database.
1. Rum 'main.py in /mysql_db_extraction to pipeline data from MySQL database to AmazonS3 bucket.
1. Run 'main.py' in /redshift_data_setup tp load data in MySQL database
1. Run 'main.py in /redshift_db_extraction to pipeline data from Amazon Redshit data warehouse to AmazonS3 bucket.
