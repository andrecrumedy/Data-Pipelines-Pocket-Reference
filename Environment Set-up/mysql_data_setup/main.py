#%% #info steps
    # step read in sql query
    # step connect to mysql database
    # step load in Orders table through sql query
    #? addtions: context manager, function for reading in all config files
    
#%% #info module imports
import pymysql
import os
import yaml
#%% #info read in text files. 
sql = open(r'conf/sql/create_orders_table.sql', 'r').read()
secrets = yaml.load(open(r'conf/secrets/creds.yaml'), Loader=yaml.FullLoader)
#%% #info connect to mysql database
conn = pymysql.connect(
    host=secrets['db_dppr-book']['host'],
    user=secrets['db_dppr-book']['user'],
    password=secrets['db_dppr-book']['password'],
    db=secrets['db_dppr-book']['db'],
    port=secrets['db_dppr-book']['port']
)
#%% #info load in Orders table through sql query
cursor = conn.cursor()
statements = sql.split(";")
for statement in statements:
    if statement.strip() != "":
        # print(statement)
        cursor.execute(statement)

conn.commit()
cursor.close()
conn.close()
#%%