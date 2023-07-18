# Setting up Amazon Redshift Database

> Purpose

- The module will serve as an automated way to create a redshift cluster.

> Notes
- For the extraction portion of this book. The authors attemps to show extraction for various data sources. To demonstrate this, these data sources must be set-up first. For Amazon Redshift, the author recommends the following AWS console instruction to set this up. Once set-up, the console query editor can be used to upload data. In practice, best practice is to use infrastructure as code for cluster set-up and configuration and also a pipeline to load the data. 
- OrdersID Data type must be BIGINT for pandas int64, it's probably best practice to use BIG data type for all int variations. 

> `Upcoming Improvements`
- Use IaC to create and deploy AWS Redshift cluster, use pipeline to load inital data (stored locally or S3 bucket) into Redshift cluster. 
- 