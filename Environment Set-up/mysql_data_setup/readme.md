# Setting Up MySQL Database for Extraction showcase  
>Purpose  
- For repeatability of this project, I have made this module which connects and loads data into the instance for use by the "mysql_db_extracion" module.

>Module Structure
- /conf: configuration files such as secrets, credentials, queries, etc.
- main.py: main script to load data in MySQL isntance. 

>Notes

- The book reccomends AWS documentation on how to use Amazon RDS to set-up a MySQL instance. It also provide the query which creates and populates this database. 
- The author does not provide instructions on connecting and querying this MySQL instance. The AWS documentation does give guidelines on connecting and querying using MySQL Workbench GUI appplication. 

> `Upcoming Improvements`
- create the MySQL instance on Amazon RDS programatically(through awswrangular or terraform) which fully automates this project