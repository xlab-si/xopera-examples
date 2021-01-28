# xOpera deploy for connecting Azure and AWS platforms
This is a simple xOpera deploy that connects Azure and AWS cloud providers.

## Table of Contents
  - [Purpose](#purpose)
  - [Content](#content)
  - [Functionality](#functionality)

## Purpose
These two folders contain repositories that implement Azure<->AWS connection and data flow from Azure to AWS and vice versa.

## Content
In `aws-azure` folder data flows from AWS S3 to Azure Containers and in `azure-aws` there is a transfer of data from Azure to AWS.

## Functionality
The main functionality of this solution is to sequentially execute two operations on images which are image-watermark and image-resize
on two different platforms (Azure and AWS). Orchestration creates 2 containers on Azure and 2 buckets on AWS. Images are passed from container
to bucket using AWS lambda or Azure function.

The two processes are shown on image below.

![alt text](connection.png "Azure<->AWS connection process diagram")
