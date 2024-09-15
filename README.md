# Fuel-Management-Application
Creating an application to manage fuel states tanks full every time by Streaming Ingestion using AWS Cloud. 

### Requirements for this project:
Need a AWS Account or AWS login credentials.

### Description:
  This repository contains the reference related to how to Manage Fuel in Multiple Stations to not become empty in Real time.

### Problem Statement:
    Need a cloud environment for managing multiple fuel/gas stations to maintance atleast more than some percent of fuel.

### Solution:
    To achieve the requirement of maintaining atleast fuel in the tank and fill the tank when needed.
    1.we need to collect the data at every specific time interval.
    2.Store that fuel data.
    3.Analyse & identify which fuel station fuel tank has less fuel than required from stored fuel data.
    4.store the fuel tanks required fuel stations data. 
    5.Immediately sent the fuel tanks to the fuel station which require fuel.


1.we need to collect the data at every specific time interval:
this can become done by the maintainer present at the fuel station.

In real time we need to stream the data from our application to storage service:

     Amazon Streaming & delivery service: Amazon Kinesis Firehose

2.Store that fuel data.
for doing this we need a data lake because we might need to store the records for future purpose for furture business plans.

      Cloud Storage Service: Amazon S3 service

We need to make the Aamzon s3 as highly serarchable datalake for future purpose

      Cloud ETL(Extracting,Transforming,Loading) tool: AWS Glue 
      In Glue we need to create database,table for analyse using athena.


3.Analyse & identify which fuel station fuel tank has less fuel than required from stored fuel data.
to Analyse & identify we need a compute service

    Cloud Compute Service: Amazon Lambda

![FuelPlanningApp Source Code](https://github.com/Srisrijakka1/Fuel-Management-Application/blob/main/FuelPlanningApp.py)

4.store the fuel tanks required fuel stations data
to store and process every request once

    Cloud queue Service: Amazon SQS 

5.Immediately sent the fuel tanks to the fuel station which require fuel
to get the fuel station data from queue we need a compute service

    Cloud Compute Service: Amazon Lambda
    
![FuelTruckApp Source Code](https://github.com/Srisrijakka1/Fuel-Management-Application/blob/main/FuelTruckApp.py)

![Fuel-Management-Application Source Code Zip file](https://github.com/Srisrijakka1/Fuel-Management-Application/blob/main/Fuel-Management-Application.zip)

### Architecture:
![Fuel-Management-Application-Architecture](https://github.com/user-attachments/assets/53f99aa1-3ca0-470c-97cd-1e95b3e0cb9f)

### Result:
https://github.com/user-attachments/assets/d4a05815-04fa-4936-a0ff-3fc8b1c50a07

