import json
import os
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

def save_user_data(username, user_data):
    # Connect to MongoDB
    client = MongoClient('mongodb://localhost:27017')
    # Select database and collection
    db = client['your_database_name']
    collection = db['your_collection_name']
    # Save user data to MongoDB
    collection.insert_one(user_data)

while True:
    tiktok_username = input("Enter TikTok username (or 'q' to quit): ")
    if tiktok_username.lower() == 'q':
        break

    try:
        source = requests.get(f'https://www.tiktok.com/@{tiktok_username}')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        # ... Your existing code to scrape TikTok user data ...

        user_data = {
            'Username': tiktok_username,
            'Profile Picture': user_profile_picture,
            'Total Followers': user_total_followers,
            'Total Following': user_total_following,
            'Total Likes': user_total_likes,
            'Videos': video_data
        }

        save_user_data(tiktok_username, user_data)

        print(f"User '{tiktok_username}' data saved to MongoDB")
        print('-------------------------------------------------------------')

    except Exception as e:
        print(e)
