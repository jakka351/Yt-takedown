import os
import requests
import json

API_KEY = 'YOUR_API_KEY'
CHANNEL_ID = 'YOUR_CHANNEL_ID'
COPYRIGHT_EMAIL = 'YOUR_EMAIL'

def get_video_ids():
    video_ids = []
    url = f'https://www.googleapis.com/youtube/v3/videos?part=id,snippet&channelId={CHANNEL_ID}&maxResults=100&key={API_KEY}'
    response = requests.get(url)
    data = response.json()

    for item in data['items']:
        video_ids.append(item['id']['videoId'])

    return video_ids

def submit_takedown_request(video_id):
    data = {
        'violationType': 'Infringement',
        'infringementType': 'DMCA',
        'reasonId': 'claimed_content_matches_existing_content_owned_by_others',
        'description': 'This video infringes on my copyright. Please remove it immediately.'
    }

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Bearer {API_KEY}',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36'
    }

    url = f'https://studio.youtube.com/copyright/takedown?vi={video_id}&feature=copyright&email={COPYRIGHT_EMAIL}'
    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        print(f'Takedown request submitted successfully for video {video_id}')
    else:
        print(f'Error submitting takedown request for video {video_id}: {response.status_code}')

def main():
    video_ids = get_video_ids()
    for video_id in video_ids:
        submit_takedown_request(video_id)

if __name__ == '__main__':
    main()
