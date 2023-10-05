# controllers/social_media_controller.py

from flask import jsonify
from services.social_media_service import get_all_reddit_posts, get_sentiment_data, get_reddit_data, get_youtube_data

def get_reddit_scores():
    try:
        # Call the service function to get all Reddit posts
        posts = get_all_reddit_posts()
        
        return posts  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_sentiment_analysis_data():
    try:
        # Call the service function to get all Reddit posts
        posts = get_sentiment_data()
        
        return posts  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_reddit_details():
    try:
        # Call the service function to get all Reddit posts
        details = get_reddit_data()
        
        return details  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_youtube_details():
    try:
        # Call the service function to get all Reddit posts
        details = get_youtube_data()
        
        return details  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")