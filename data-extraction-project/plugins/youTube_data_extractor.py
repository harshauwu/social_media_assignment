import googleapiclient.discovery
import pandas as pd

def extract_video_data(**kwargs):
    ti = kwargs['ti'] 

    # Set your API key here
    api_key = 'AIzaSyDqo_SDsaZimlGsa7QUdl47yBMArVqKUTA'

    # Create a YouTube Data API client
    youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

    # Define the channelId of the YouTube channel you want to fetch videos from
    channel_id = 'UCucZ0dYXTXLs66eKo98ujmg'

    # Use the search.list method to retrieve a list of videos from the channel
    search_response = youtube.search().list(
        q=None,
        type='video',
        channelId=channel_id,
        order='date',
        part='id',
        maxResults=500  # You can adjust this to retrieve more or fewer videos
    ).execute()

    # Extract video IDs from the search results
    video_ids = [item['id']['videoId'] for item in search_response['items']]

    print(video_ids)

    # Fetch video details for each video ID
    video_details = []

    for video_id in video_ids:
        video_response = youtube.videos().list(
            part='snippet, contentDetails, statistics',
            id=video_id
        ).execute()
        
        # Extract video details from the response
        video_info = video_response['items'][0]
        
        # Extract relevant details such as title, description, and view count
        title = video_info['snippet']['title']
        published_at = video_info['snippet']['publishedAt']
        description = video_info['snippet']['description']
        view_count = video_info['statistics']['viewCount']
        like_count = video_info['statistics']['likeCount']
        comment_count = video_info['statistics']['commentCount']
        favorite_count = video_info['statistics']['favoriteCount']
        duration_count = video_info['contentDetails']['duration']
        published_at = video_info['snippet']['publishedAt']
        
        # Store the video details in a dictionary
        video_detail = {
            'title': title,
            'description': description,
            'view_count': view_count,
            'like_count' : like_count,
            'comment_count' : comment_count,
            'favorite_count' : favorite_count,
            'durations' :duration_count,
            'published_at' :  published_at
        }
        
        video_details.append(video_detail)

    df = pd.DataFrame(video_details)   
    print(df)

    # Specify the path where you want to save the CSV file
    csv_file_path = "/home/airflow/starbucks_post_data_raw.csv"
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

    ti.xcom_push(key='youTube_vide_raw_data', value=csv_file_path)