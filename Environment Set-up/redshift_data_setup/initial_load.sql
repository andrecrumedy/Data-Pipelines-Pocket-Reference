'''
Scripts ran directly in AWS console for through aweb browser for data loading 
'''

--script to create schema
CREATE SCHEMA IF NOT EXISTS dppr_book;

-- script to create order table
CREATE TABLE dppr_book.Orders(
    OrderID BIGINT,
    OrderStatus VARCHAR(30),
    LastUpdated TIMESTAMP
);

-- script to use in AWS console query editor for copying for Amazon S3 bucket
COPY dppr_book.orders
FROM 's3://dppr-book/orders.parquet'
IAM_ROLE 'arn:aws:iam::931383613702:role/service-role/AmazonRedshift-CommandsAccessRole-20230712T113738'
FORMAT AS PARQUET;


-- script to update table column type
ALTER TABLE dppr_book.orders
ALTER COLUMN OrderID TYPE BIGINT

--script to drop table
DROP TABLE IF EXISTS dppr_book.orders;

--script to see data in the data warehouse
