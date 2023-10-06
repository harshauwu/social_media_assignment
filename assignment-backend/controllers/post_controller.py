from flask import request, jsonify
import praw
from praw.models import InlineGif, InlineImage, InlineVideo
from config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET, REDDIT_USER_AGENT
from services.post_service import save_post, get_all_schedule_posts


def get_schedule_posts():
    try:
         
       # Call the service function to get all Reddit posts
        posts = get_all_schedule_posts()
        return posts
    
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"

def create_schedule_post():
    try:
         
        # Get post data from the form
        data = request.get_json()
        new_post = save_post(data)

        # if new_post.id:
        #     if data.is_one_time:
        #          print('sdf')
                # create_reddit_post(data)
                # create_facebook_post(data)
        return jsonify(data)  
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"

def create_reddit_post(data):
    try:
        # Initialize the Reddit API client
        reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                            client_secret=REDDIT_CLIENT_SECRET,
                            user_agent=REDDIT_USER_AGENT,
                            username="Global-Tomatillo-248",
                            password="AdAiAY#JDS1",
                            redirect_uri='http://localhost:5050/callback')
    
        
        title = data.title
        self_text = data.text

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
     print('this is facebook api~')
         