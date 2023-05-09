# Project Description


A data engineering project for obtaining TikTok user account information and loading it into Azure Blob Storage can have a business premise of conducting market research, improving user engagement, or enhancing the overall TikTok user experience.

The project can be divided into three main stages: data collection, data processing, and data analysis.

1. Data collection and migration stage: The project would involve scraping the TikTok platform for user account information. This information can include the number of followers, the number of likes, the user's country of origin, and other relevant information. Once the data has been collected, it would be loaded into Azure Blob Storage.


![3](https://github.com/HelloSongi/TikTok-User-data-analysis/assets/69304233/12f58472-c68c-4f3f-afee-ab0446bd9c2b)

Use Azcopy function to upload data to azure blob storage

```
azcopy copy "C:\local\path" "https://account.blob.core.windows.net/mycontainer1/?sv=2018-03-28&ss=bjqt&srt=sco&sp=rwddgcup&se=2019-05-01T05:01:17Z&st=2019-04-30T21:01:17Z&spr=https&sig=MGCXiyEzbtttkr3ewJIh2AR8KrghSy1DGM9ovN734bQF4%3D" --recursive=true
```

2. Data processing stage: The data would be aggregated and cleaned using Databricks with Pyspark. This process would involve filtering out any duplicate or irrelevant data, as well as transforming the data into a format that can be easily analyzed.

3. Data analysis stage: the cleaned data would be fed into Power BI for analysis. This would allow stakeholders to gain insights into user behavior and preferences, as well as identify areas for improvement in the TikTok platform.

Overall, the project would help TikTok better understand its users and improve the overall user experience on the platform.
