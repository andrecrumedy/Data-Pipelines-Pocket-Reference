# MySQL DB Extraction
> Purpose

- The package contains pipelines for full and incremental extraction. The author uses MySQL for source of full extraction, Amazon S3 bucket as data lake(file system sotrage), and Amazon Redshit data warehouse as a destination, all hosted on AWS. 

>Module Structure

- /conf: configuration files such as secrets, and app parameters, sql queries, etc.
- extraction.py: 
    - all extraction code will be contained in one module. All the extracted data will be loaded in Amazon S3 bucket.
    - Moving from the authors recommendations of having a separate module for each pipelines, I've combined all three pipeliens into one module: Full extraction from MySQL, Full Extraction from AWS Redshift(`as a bonus`), and incremental extraction from MySQL

>Notes
- Differences  
    - I do not use configparser and .conf files, my preference is PyYAML and .yaml file for configuration. 
    - I also prefer not to write SQL directly in python script, rather keep them separate in their on ,sql file and read in a text configuration file.
    - I incorporate the use of context management with connecting to databases and use pandas read_sql method for reading the database table directly into a Dataframe. This way I do not have the store the table ina local file, modifying application files. 
    - awswrangular is used to write to S3 bucket. 
    - AWS redshift.connector is used to query Redshift in lieu of psycogg2
    - extra steps included to verify and delete the uploaded S3 object.

> `Upcoming Improvements`
- create a function to read all configuration files in at once and then set quick access variables
- store and retrieve credential/connection information in a key vault, providing greater security and more code flexibility.

