import json
import os
import pandas as pd

# Import the extract_tiktok_data.py module
from extract_tiktok_data import user_video_data

# Process user data
user_data_list = []
total_views = 0

for user_video in user_video_data:
    user_data = user_video['User']
    total_views += sum(int(video['Views']) for video in user_video['Videos'])
    user_data_list.append(user_data)

# Create a DataFrame for user data
user_df = pd.DataFrame(user_data_list)

# Calculate total views from all videos
total_views_data = {'Total Views': total_views}
total_views_df = pd.DataFrame([total_views_data])

# Process video data
video_data_list = []

for user_video in user_video_data:
    for video in user_video['Videos']:
        video_data = {
            'Video_title': video['Video_title'],
            'Views': video['Views'],
            'Likes': video['Likes'],
            'Link': video['Link']
        }
        video_data_list.append(video_data)

# Create a DataFrame for video data
video_df = pd.DataFrame(video_data_list)

# Sort videos by views and select top 5
top_videos_views = video_df.sort_values(by='Views', ascending=False).head(5)

# Sort videos by likes and select top 5
top_videos_likes = video_df.sort_values(by='Likes', ascending=False).head(5)

# Create a dictionary to store processed data
processed_data = {
    'User Data': user_df.to_dict(orient='records'),
    'Total Views': total_views_df.to_dict(orient='records'),
    'Top Videos by Views': top_videos_views.to_dict(orient='records'),
    'Top Videos by Likes': top_videos_likes.to_dict(orient='records')
}

# Save processed data as JSON file
folder_path = "processed_data"
if not os.path.exists(folder_path):
    os.makedirs(folder_path)

json_file_path = os.path.join(folder_path, "processed_data.json")
with open(json_file_path, 'w') as json_file:
    json.dump(processed_data, json_file, indent=4)

print("Data processing complete. Processed data saved as 'processed_data.json'.")
