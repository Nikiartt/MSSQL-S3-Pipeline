# MSSQL-S3-Pipeline

# Introduction & Goals
In this mini project, I learned how to create simple connections between Microsoft SQL Server and AWS S3 service using Python. The goal was to learn how to load data to MSSQL, extract data, reorganize and split it into multiple files, and store it to AWS S3 from external software. The pipeline demonstrated load velocity to MSSQL of 7.12 MB/second. 

# Contents

- [The Data Set](#the-data-set)
- [Used Tools](#used-tools)
- [Pipeline](#pipeline)
- [Pipeline testing](#pipeline-testing)
- [Conclusion](#conclusion)
- [LinkedIn Profile](#linkedin-profile)


# The Data Set
The free global COVID data set was used from open source (https://data.humdata.org/dataset/coronavirus-covid-19-cases-and-deaths?). The data contains information about new and cumulative cases over different countries in the range of 2020-01-05 and 2023-12-31.

# Used Tools
- Microsoft SQL Server was set up on a local machine.
- In Python, I used libraries such as pandas, time, requests, pyodbc, boto3, and pydantic-settings.
- I chose AWS S3 storage by the reason that it provides the ability to use AWS services such as Glue or Kinesis in the future.

# Pipeline
The batch ELT pipeline allows users to adjust different connection parameters like MSSQL bucket name, MSSQL server, and database names, and access keys for the AWS bucket using a .env file. The transaction stages of data are stored on the local machine in the "data" folder(this can be used for testing and checking different parameters). The main connections were built on pyodbc and boto3 libraries.


# Pipeline testing
The testing time system is implemented directly in the code. 

# Conclusion
The batch ELT pipeline provides the user the ability to adjust different connection parameters like MSSQL bucket name, MSSQL server and database names, and access keys for the AWS bucket using a .env file. The transaction stages of data are stored on the local machine in the "data" folder(this can be used for testing and checking different parameters). The main connections were built on pyodbc and boto3 libraries.

# LinkedIn Profile
- www.linkedin.com/in/arturas-nikitinas
