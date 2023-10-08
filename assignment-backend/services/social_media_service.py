from flask import jsonify
from db.models.reddit_posts import RedditPost  # Import the RedditPost model
from db.models.youtube_posts import YoutubePost
from db.models.organization_table import OrganizationTable 
from db.models.reddit_post_comments import RedditPostComment
from collections import Counter
import pickle
import pandas as pd
from statsmodels.tsa.arima_model import ARIMA
import statsmodels.api as sm
import json
import networkx as nx

def get_all_reddit_posts():
    """
    Retrieve all Reddit posts from the database.
    Returns a list of RedditPost objects.
    """
    try:
        posts = RedditPost.query.all()
        posts_data = []
        for post in posts:
            reddit_post_dict = {
                "title": post.title,
                "post_id": post.post_id,
                "score": post.score,
                "id": post.id,
                "url": post.url,
                "comms_num": post.comms_num,
                "created": post.created,
                "body": post.body,
                "author": post.author,
                "subreddit": post.subreddit
            }
            posts_data.append(reddit_post_dict)
        return posts_data
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"

def get_sentiment_data():
    try:
        sentiments = []
        post_comments = RedditPostComment.query.all()
        for comment in post_comments:
            sentiment_data = comment.sentiment 

            # Append the sentiment information to the list
            sentiments.append(sentiment_data)

        sentiment_counts = Counter(sentiments)  
        positive_count = sentiment_counts['positive']
        neutral_count = sentiment_counts['neutral']
        negative_count = sentiment_counts['negative']  

        data = {'positive':positive_count ,'neutral': neutral_count, 'negative': negative_count}
        return data
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"   

def get_reddit_data():
    try:
        like_count = 0
        comment_count = 0

        posts = RedditPost.query.all()
        reddit = OrganizationTable.query.filter_by(social_media_platform='Reddit').first()
        subscribers = reddit.subscribers
       
        for post in posts:
            like_count = like_count + post.score
            comment_count =  comment_count + post.comms_num

        data = {'like_count': like_count, 'comment_count': comment_count, 'subscriber_count': subscribers}

        return data
    
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
    
def get_youtube_data():
    try:
        view_count = 0
        like_count = 0
        comment_count = 0
        
        posts = YoutubePost.query.all()
        youtube = OrganizationTable.query.filter_by(social_media_platform='YouTube').first()
        subscribers = youtube.subscribers

        for post in posts:
            view_count = view_count + post.view_count
            like_count = like_count + post.like_count
            comment_count =  comment_count + post.comment_count
            
        data = {'like_count': like_count, 'comment_count': comment_count, 'view_count': view_count, 'subscriber_count': subscribers}
        return data
    
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
    

def get_reddit_like_forecasts(forecast_periods):
    """Generates forecasts for Reddit likes using a trained ARIMA model.

    Args:
        forecast_periods: The number of periods to forecast.

    Returns:
        A JSON string containing the forecasted values and dates.
    """
    model_save_path = '/app/ml_models/arima/arima_reddit_like_model.pkl'

    # Load the trained ARIMA model
    with open(model_save_path, 'rb') as model_file:
        loaded_arima_model = pickle.load(model_file)


    # Get the last date for which we have data
    last_date = '2023-08-22 00:00:00'
    last_date = pd.to_datetime(last_date)

    try:
        # Generate forecasts using the loaded ARIMA model
        forecasts = loaded_arima_model.forecast(steps=forecast_periods)

        # Validate the forecast dates
        forecast_dates = pd.date_range(start=last_date + pd.DateOffset(1), periods=forecast_periods)
        if not all(forecast_dates > last_date):
            raise Exception('Forecast dates must be in the future.')

        # Extract only the date part
        forecast_dates = forecast_dates.date

        # Assuming forecast_dates is a NumPy array
        forecast_dates = pd.to_datetime(forecast_dates)

        # Extract only the date part
        forecast_dates = forecast_dates.date

        # Create a DataFrame to store the forecasted values and dates
        forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecasts})

        # Convert the DataFrame to the desired format
        data = []
        for index, row in forecast_df.iterrows():
            data_point = {"x": str(row['Date']), "y": round(row['Forecast'])}
            data.append(data_point)

        forecast_data = [
            {
                "id": "likes",
                "color": "hsl(99, 70%, 50%)",
                "data": data
            }
        ]
                
        return forecast_data
    except Exception as e:
        # Return an error message if anything goes wrong
        return f"Error fetching Reddit posts: {str(e)}"


def get_youtube_view_forecasts(forecast_periods):

    model_save_path = '/app/ml_models/arima/arima_youtube_view_model.pkl'

    # Load the trained ARIMA model
    with open(model_save_path, 'rb') as model_file:
        loaded_arima_model = pickle.load(model_file)

    # Get the last date for which we have data
    last_date = '2023-09-10 00:00:00'
    last_date = pd.to_datetime(last_date)

    try:
        # Generate forecasts using the loaded ARIMA model
        forecasts = loaded_arima_model.forecast(steps=forecast_periods)

        # Validate the forecast dates
        forecast_dates = pd.date_range(start=last_date + pd.DateOffset(1), periods=forecast_periods)
        if not all(forecast_dates > last_date):
            raise Exception('Forecast dates must be in the future.')

        # Extract only the date part
        forecast_dates = forecast_dates.date

        # Assuming forecast_dates is a NumPy array
        forecast_dates = pd.to_datetime(forecast_dates)

        # Extract only the date part
        forecast_dates = forecast_dates.date

        # Create a DataFrame to store the forecasted values and dates
        forecast_df = pd.DataFrame({'Date': forecast_dates, 'Forecast': forecasts})

        # Convert the DataFrame to the desired format
        data = []
        for index, row in forecast_df.iterrows():
            data_point = {"x": str(row['Date']), "y": round(row['Forecast'])}
            data.append(data_point)

        forecast_data = [
            {
                "id": "likes",
                "color": "hsl(99, 70%, 50%)",
                "data": data
            }
        ]
                
        return forecast_data

    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"        


def get_network_analysis_details():
    try:
        relationships = []
        post_comments = RedditPostComment.query.all()
        for comment in post_comments:
            data = {
                "post_author":comment.post_author,
                "comment_auther": comment.comment_auther
            }

            # Append the relationships information to the list
            relationships.append(data)

        # Convert the list of dictionaries to a pandas DataFrame
        df = pd.DataFrame(relationships) 

        # Handle Missing Values (NaN)
        df.dropna(subset=['comment_auther'], inplace=True)

        # Create an empty graph
        G = nx.Graph()

        # Add nodes and edges based on the DataFrame
        for _, row in df.iterrows():
            post_author = row['post_author']
            comment_author = row['comment_auther']
            
            # Add nodes for post authors and comment authors
            G.add_node(post_author)
            G.add_node(comment_author)
            
            # Add an edge between post author and comment author
            G.add_edge(post_author, comment_author)   
        
        degree_centrality_data = degree_centrality(G)
        betweenness_centrality_data = betweenness_centrality(G)
        closeness_centrality_data = closeness_centrality(G)

        return {'degree_centrality': degree_centrality_data, 'betweenness_centrality': betweenness_centrality_data, 'closeness_centrality': closeness_centrality_data}
    except Exception as e:
            # Handle exceptions (e.g., database connection error)
            return f"Error fetching Reddit posts: {str(e)}"  
    
def degree_centrality(G): 
    # Calculate degree centrality for each author
    degree_centrality = nx.degree_centrality(G)

    # Sort authors by degree centrality in descending order
    sorted_authors_by_degree = sorted(degree_centrality.items(), key=lambda x: x[1], reverse=True)

    # Print authors with the highest degree centrality values
    num_top_authors = 5  # You can change this number to get more or fewer top authors
    top_authors = sorted_authors_by_degree[:num_top_authors]

    degree_centrality_data = []
    for author, centrality in top_authors:
        data = {
            "node": author,
            "centrality":centrality
        }
        degree_centrality_data.append(data)

    return degree_centrality_data

def betweenness_centrality(G):

    # Calculate betweenness centrality
    betweenness_centrality = nx.betweenness_centrality(G)
    
    num_top_authors = 5  # You can change this number to get more or fewer top authors
    
    # Sort authors by betweenness centrality in descending order
    sorted_authors_by_betweenness = sorted(betweenness_centrality.items(), key=lambda x: x[1], reverse=True)

    # Print authors with the highest betweenness centrality values
    between_top_authors = sorted_authors_by_betweenness[:num_top_authors]

    betweenness_centrality_data = []
    for node, centrality in between_top_authors:
        data = {
            "node": node,
            "centrality":centrality
        }
        betweenness_centrality_data.append(data)
    return  betweenness_centrality_data   


def closeness_centrality(G):

    num_top_authors = 5  # You can change this number to get more or fewer top authors

    # Calculate closeness centrality
    closeness_centrality = nx.closeness_centrality(G)

    # Sort authors by betweenness centrality in descending order
    sorted_authors_by_closeness = sorted(closeness_centrality.items(), key=lambda x: x[1], reverse=True)

    # Print authors with the highest betweenness centrality values
    closeness_top_authors = sorted_authors_by_closeness[:num_top_authors]

    centrality_centrality_data = []
    for node, centrality in closeness_top_authors:
        data = {
            "node": node,
            "centrality":centrality
        }
        centrality_centrality_data.append(data)

    return centrality_centrality_data    

