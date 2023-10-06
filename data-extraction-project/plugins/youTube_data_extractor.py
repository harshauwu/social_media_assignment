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

    # Initialize a list to store all the video IDs
    all_video_ids = []

    # Perform 20 iterations to fetch videos
    for _ in range(20):
        # Use the search.list method to retrieve a list of videos from the channel
        search_response = youtube.search().list(
            q=None,
            type='video',
            channelId=channel_id,
            order='date',
            part='id',
            maxResults=50,
            # Set the pageToken to the token of the previous response (or None for the first request)
            pageToken=next_page_token if 'nextPageToken' in locals() else None
        ).execute()

        # Extract video IDs from the search results
        video_ids = [item['id']['videoId'] for item in search_response['items']]

        # Append the current page's video IDs to the list of all video IDs
        all_video_ids.extend(video_ids)

        # Get the next page token for the next iteration
        next_page_token = search_response.get('nextPageToken')

        # If there's no more next page, exit the loop
        if not next_page_token:
            break

    print(all_video_ids)

    # Fetch video details for each video ID
    video_details = []

    for video_id in all_video_ids:
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


def extract_youtube_starbucks_details(**kwargs):
    ti = kwargs['ti']
    try:
        # Set your API key here
        api_key = 'AIzaSyDqo_SDsaZimlGsa7QUdl47yBMArVqKUTA'

        # Create a YouTube Data API client
        youtube = googleapiclient.discovery.build('youtube', 'v3', developerKey=api_key)

        # Define the channelId of the YouTube channel you want to fetch details for
        channel_id = 'UCucZ0dYXTXLs66eKo98ujmg'

        # Request channel details
        channel_response = youtube.channels().list(
            part='snippet,statistics',
            id=channel_id
        ).execute()

        # Extract channel details from the response
        channel_info = channel_response['items'][0]


        # Extract relevant details such as title, name, and number of subscribers
        details = {
            'title' : channel_info['snippet']['title'],
            'display_name' : channel_info['snippet']['customUrl'],  # Use 'customUrl' to get the channel name (if available)
            'subscribers' : channel_info['statistics']['subscriberCount'],
            'social_media_platform' :  'YouTube',
            'description' : '',
            'image' : ''
        }

        posts_df = pd.DataFrame([details])    
        print(posts_df)

        # Specify the path where you want to save the CSV file
        csv_file_path = "/home/airflow/youtube_starbucks_details.csv"
        
        # Write the DataFrame to a CSV file
        posts_df.to_csv(csv_file_path, index=False)

        ti.xcom_push(key='starbucks_data', value=csv_file_path)
        
    except Exception as e:
        # Handle the exception here (e.g., log it, send an alert, etc.)
        print(f"An error occurred in initial_data_transformation: {str(e)}")
        raise e  