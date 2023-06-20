import json
import os
from pyspark.sql import SparkSession
from pyspark.sql.functions import desc

# Import the extract_tiktok_data.py module
from extract_tiktok_data import user_video_data

# Create a SparkSession
spark = SparkSession.builder.master("local").appName("TikTokDataProcessing").getOrCreate()

# Convert user video data to Spark DataFrame
user_video_df = spark.createDataFrame(user_video_data)

# Process user data
user_df = user_video_df.select("User.Username", "User.Total Followers", "User.Total Following", "User.Total Likes")

# Calculate total views from all videos
total_views = user_video_df.selectExpr("aggregate(Videos, 0L, (acc, v) -> acc + CAST(v.Views AS LONG)) AS Total_Views")

# Process video data
video_df = user_video_df.select("Videos.Video_title", "Videos.Views", "Videos.Likes", "Videos.Link")

# Sort videos by views and select top 5
top_videos_views = video_df.orderBy(desc("Views")).limit(5)

# Sort videos by likes and select top 5
top_videos_likes = video_df.orderBy(desc("Likes")).limit(5)

# Convert DataFrames to JSON strings
user_data_json = user_df.toJSON().collect()
total_views_json = total_views.toJSON().collect()
top_videos_views_json = top_videos_views.toJSON().collect()
top_videos_likes_json = top_videos_likes.toJSON().collect()

# Create a dictionary to store processed data
processed_data = {
    'User Data': [json.loads(data) for data in user_data_json],
    'Total Views': [json.loads(data) for data in total_views_json],
    'Top Videos by Views': [json.loads(data) for data in top_videos_views_json],
    'Top Videos by Likes': [json.loads(data) for data in top_videos_likes_json]
}

# Save processed data as JSON file
folder_path = "processed_data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

json_file_path = os.path.join(folder_path, "processed_data.json")
with open(json_file_path, 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

print("Data processing complete. Processed data saved as 'processed_data.json'.")
