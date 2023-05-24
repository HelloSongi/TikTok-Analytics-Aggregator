import json
import os

from bs4 import BeautifulSoup
import requests

user_video_data = []  # Empty list to store user and video data

while True:
    tiktok_username = input("Enter TikTok username: ")

    try:
        source = requests.get(f'https://www.tiktok.com/@{tiktok_username}')
        source.raise_for_status()

        soup = BeautifulSoup(source.text, 'html.parser')
        user_info = soup.find('h3', class_="tiktok-12ijsdd-H3CountInfos e1457k4r0").find_all('div')
        user_total_following = user_info[0].find('strong').text
        user_total_followers = user_info[1].find('strong').text
        user_total_likes = user_info[2].find('strong').text

        user_data = {
            'Username': tiktok_username,
            'Total Followers': user_total_followers,
            'Total Following': user_total_following,
            'Total Likes': user_total_likes
        }

        video_container = soup.find('div', class_="tiktok-yvmafn-DivVideoFeedV2 ecyq5ls0")
        videos = video_container.find_all('div', class_="tiktok-x6y88p-DivItemContainerV2 e19c29qe7")

        video_data = []
        for video in videos:
            title = video.find('img', {'class': 'tiktok-1itcwxg-ImgPoster'}).get('alt')
            link = video.find('a', {'href': True}).get('href')

            views_elem = video.find('div', {'class': 'tiktok-11u47i-DivCardFooter e148ts220'}).strong
            views = views_elem.get_text(strip=True) if views_elem else None

            likes_elem = video.find('div', {'class': 'tiktok-11u47i-DivCardFooter e148ts220'})
            likes = likes_elem.get_text(strip=True) if likes_elem else None

            video_data.append({
                'Video_title': title,
                'Views': views,
                'Likes': likes,
                'Link': link
            })

        user_video_data.append({
            'User': user_data,
            'Videos': video_data
        })

        # Save user and video data as JSON file
        folder_path = "raw_data"
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        json_file_path = os.path.join(folder_path, f"{tiktok_username}_data.json")
        with open(json_file_path, 'w') as json_file:
            json.dump(user_video_data, json_file, indent=4)

        print('User and Video Data:')
        print(json.dumps(user_video_data, indent=4))
        print('-------------------------------------------------------------')

    except Exception as e:
        print(e)
