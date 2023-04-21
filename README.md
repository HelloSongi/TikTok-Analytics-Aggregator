# Project Overview

With the help of Databricks, Spark and Azure, we were able to extract the top 10 trending topics from Twitter and Reddit and send them directly to a user's email. By leveraging the power of these cloud-based platforms, i was able to efficiently process and analyze large amounts of data, extract meaningful insights, and deliver them directly to a users in a timely manner. 

To implement this project, the steps are steps:

1. Collected the data from Twitter and Reddit using their APIs and store it in an Azure Blob Storage account.
2. Using Databricks to process the collected data and extract the top 10 trending topics from each source.
3. Merged the trending topics from both sources and filter out any duplicates.
4. Useing Azure Functions to trigger an email containing the trending topics to the user's email address.


Detailed breakdown of each step:

1. Collecting Data: Used Twitter and Reddit APIs to collect data related to trending topics. Created a Python script that connects to the APIs and retrieves data for a specific time range. Then, stored the data in an Azure Blob Storage account.

2. Processing Data: Created a Databricks notebook to read the data from the Azure Blob Storage account, process it using Spark and extract the top 10 trending topics from each source.

3. Merging Data: Combined the trending topics from both sources using the union() method in Spark and then filter out any duplicates.

4. Sending Email: Create an Azure Function that triggers periodically and reads the merged data from Azure Blob Storage. The function can then use an SMTP library to send an email containing the trending topics to the user's email address.

5. Finally, scheduled the Databricks notebook and Azure Function to run periodically and update the user with the latest trending topics.
