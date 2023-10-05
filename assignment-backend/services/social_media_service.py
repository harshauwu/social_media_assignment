from flask import jsonify
from db.models.reddit_posts import RedditPost  # Import the RedditPost model
# from db.models.reddit_post_comments import RedditPostComment  # Import the RedditPostComment model

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
        return jsonify(posts_data)
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"

def get_sentiment_data():
    try:
        # posts = RedditPostComment.query.all()
        posts_data = []
        return jsonify(posts_data)
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"    