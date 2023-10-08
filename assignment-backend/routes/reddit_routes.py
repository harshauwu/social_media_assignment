# routes/reddit_routes.py
from flask import Blueprint, jsonify
from controllers import social_media_controller, post_controller

# Create a Blueprint for your Reddit routes
reddit_routes = Blueprint('reddit_routes', __name__)

@reddit_routes.route("/posts-score",  methods=['GET'])
def get_reddit_score():
    scores = social_media_controller.get_reddit_scores()
    return scores

@reddit_routes.route('/schedule-post', methods=['POST'])
def create_schedule_post():
    post = post_controller.create_schedule_post()
    return post

@reddit_routes.route('/schedule-post', methods=['GET'])
def fetch_schedule_post():
    posts = post_controller.get_schedule_posts()
    return posts

@reddit_routes.route('/comment-polarity', methods=['GET'])
def fetch_analyze_sentiment():
    sentiment_analysis = social_media_controller.get_sentiment_analysis_data()
    return sentiment_analysis

@reddit_routes.route('/predictive-likes', methods=['GET'])
def fetch_predictive_likes():
    predictive_likes = social_media_controller.get_predict_likes()
    return predictive_likes

@reddit_routes.route('/reddit-details', methods=['GET'])
def fetch_reddit_details():
    reddit_details = social_media_controller.get_reddit_details()
    return reddit_details

@reddit_routes.route('/youtube-details', methods=['GET'])
def fetch_youtube_details():
    reddit_details = social_media_controller.get_youtube_details()
    return reddit_details

@reddit_routes.route('/predictive-views', methods=['GET'])
def fetch_predictive_views():
    predictive_views = social_media_controller.get_predict_views()
    return predictive_views

@reddit_routes.route('/social-network-analysis', methods=['GET'])
def fetch_analysis_details():
    predictive_views = social_media_controller.social_network_analysis()
    return predictive_views