from flask import request, jsonify
import praw
from praw.models import InlineGif, InlineImage, InlineVideo
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT, REDDIT_USER_NAME, REDDIT_PASSWORD, PAGE_ACCESS_TOKEN, PAGE_ID
from services.post_service import save_post, get_all_schedule_posts
import requests

def get_schedule_posts():
    try:
       # Call the service function to get all Reddit posts
        posts = get_all_schedule_posts()
        return jsonify({"data": posts}), 200
    
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"

def create_schedule_post():
    try:
        # Get post data from the form
        data = request.get_json()
        new_post = save_post(data)

        if new_post.id:
            if data['is_one_time']:
                data = create_reddit_post(data)
                create_facebook_post(data)
        return jsonify({"message": "schedule post insert successful", "id": new_post.id, "data": data}), 200
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error Saving Reddit posts: {str(e)}"

def create_reddit_post(data):
    try:
        # Initialize the Reddit API client
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                            client_secret=REDDIT_CLIENT_SECRET,
                            user_agent=REDDIT_USER_AGENT,
                            username=REDDIT_USER_NAME, 
                            password=REDDIT_PASSWORD, 
                            redirect_uri='http://localhost:5050/callback')
    
        
        title = data["title"]
        self_text = data["text"]

        # gif = InlineGif(path="path/to/image.gif", caption="optional caption")
        image = InlineImage(path="media/test.png", caption="this is test image")
        # video = InlineVideo(path="path/to/video.mp4", caption="optional caption")
        # media = {"gif1": gif, "image1": image, "video1": video}
        media = {"image1": image}
        
        created_post = reddit.subreddit("pythonsandlot").submit(title, selftext=self_text, inline_media=media)
        
        return {'data' : created_post.title}
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"

def create_facebook_post(data):
    try: 

        # Your Facebook App ID
        FACEBOOK_PAGE_ID = PAGE_ID

        # Your Facebook Page Access Token
        FACEBOOK_PAGE_ACCESS_TOKEN = PAGE_ACCESS_TOKEN

        # The Facebook Graph API endpoint for publishing posts
        FACEBOOK_GRAPH_API_ENDPOINT = f'https://graph.facebook.com/v18.0/{FACEBOOK_PAGE_ID}/feed'

         # Create a POST request to the Facebook Graph API endpoint
        request = requests.post(
            FACEBOOK_GRAPH_API_ENDPOINT,
            headers={
                'Authorization': 'Bearer {}'.format(FACEBOOK_PAGE_ACCESS_TOKEN)
            },
            data={
                'message': data['text']
            }
        )

        # Check if the request was successful
        if request.status_code == 200:
            return True
        else:
            return False
        
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"
         