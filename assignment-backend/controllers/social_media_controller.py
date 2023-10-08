# controllers/social_media_controller.py

from flask import request, jsonify
from services.social_media_service import get_all_reddit_posts, get_sentiment_data, get_reddit_data, get_youtube_data, get_reddit_like_forecasts, get_youtube_view_forecasts, get_network_analysis_details

def get_reddit_scores():
    try:
        # Call the service function to get all Reddit posts
        posts = get_all_reddit_posts()
        
        return jsonify({"data": posts}), 200  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_sentiment_analysis_data():
    try:
        # Call the service function to get all Reddit posts
        posts = get_sentiment_data()
        
        return jsonify({"data": posts}), 200   # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_reddit_details():
    try:
        # Call the service function to get all Reddit posts
        details = get_reddit_data()
        
        return jsonify({"data": details}), 200   # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_youtube_details():
    try:
        # Call the service function to get all Reddit posts
        details = get_youtube_data()
        
        return jsonify({"data": details}), 200  # Return the calculated scores
        
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        print(f"Error getting Reddit scores: {str(e)}")

def get_predict_likes():
    try:
        # Get the 'forecast_periods' query parameter from the URL
        forecast_periods = request.args.get('forecast_periods')

        # Convert the parameter to an integer (assuming it's an integer)
        forecast_periods = int(forecast_periods)

        # Call the service function to get all Reddit posts
        posts = get_reddit_like_forecasts(forecast_periods)
        return jsonify({"data": posts}), 200 
    
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"


def get_predict_views():
    try:
        # Get the 'forecast_periods' query parameter from the URL
        forecast_periods = request.args.get('forecast_periods')

        # Convert the parameter to an integer (assuming it's an integer)
        forecast_periods = int(forecast_periods)

        # Call the service function to get all Reddit posts
        posts = get_youtube_view_forecasts(forecast_periods)
        return jsonify({"data": posts}), 200
    
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"
    
def social_network_analysis():
    try:
       network_details = get_network_analysis_details()  
       return jsonify({"data": network_details}), 200  
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"