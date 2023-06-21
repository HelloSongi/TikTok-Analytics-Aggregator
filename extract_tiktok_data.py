import os
import json
from bs4 import BeautifulSoup
import requests
from pymongo import MongoClient

def save_user_data(username, user_data):
    # Connect to MongoDB
    client = MongoClient('mongodb+srv://song:1181750032@cluster0.kiid4gt.mongodb.net/')
    # Select database and collection
    db = client['tiktok_data']
    collection = db['tiktok']
    # Save user data to MongoDB
    collection.insert_one(user_data)

def convert_value_to_int(value):
    if value.endswith('K'):
        return int(float(value[:-1]) * 1000)
    elif value.endswith('M'):
        return int(float(value[:-1]) * 1000000)
    elif '.' in value:
        return int(float(value))
    else:
        return int(value)

while True:
    tiktok_username = input("Enter TikTok username (or 'q' to quit): ")
    if tiktok_username.lower() == 'q':
        break

    try:
        source = requests.get(f'https://www.tiktok.com/@{tiktok_username}')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        user_info = soup.find('h3', class_="tiktok-12ijsdd-H3CountInfos e1457k4r0").find_all('div')
        user_profile_picture = soup.find('img', class_="tiktok-1zpj2q-ImgAvatar").get('src')
        user_total_following = user_info[0].find('strong').text
        user_total_followers = user_info[1].find('strong').text
        user_total_likes = user_info[2].find('strong').text

        user_total_followers = convert_value_to_int(user_total_followers)
        user_total_following = convert_value_to_int(user_total_following)
        user_total_likes = convert_value_to_int(user_total_likes)

        video_container = soup.find('div', {'class': 'tiktok-yvmafn-DivVideoFeedV2 ecyq5ls0'})
        if video_container:
            videos = video_container.find_all('div', class_="tiktok-x6y88p-DivItemContainerV2 e19c29qe8")
        else:
            videos = []

        video_data = []
        user_total_views = 0
        for video in videos:
            title = video.find('img', {'class': 'tiktok-1itcwxg-ImgPoster'}).get('alt')
            link = video.find('a', {'href': True}).get('href')

            views_elem = video.find('div', {'class': 'tiktok-11u47i-DivCardFooter e148ts220'}).find_all('strong')
            view = views_elem[0].text if views_elem else None

            views = convert_value_to_int(view) if view else None

            user_total_views = user_total_views + views
            video_data.append({
                'Video_title': title,
                'Views': views,
                'Link': link
            })

        user_data = {
            'Username': tiktok_username,
            'Profile Picture': user_profile_picture,
            'Total Followers': user_total_followers,
            'Total Following': user_total_following,
            'Total Video Likes': user_total_likes,
            'Totaol Video Views': user_total_views,
            'Videos': video_data
        }

        save_user_data(tiktok_username, user_data)
        print(f"User '{tiktok_username}' data saved to MongoDB")
        print('-------------------------------------------------------------')

    except Exception as e:
        print(e)

