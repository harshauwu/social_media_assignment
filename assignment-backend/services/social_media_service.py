from flask import jsonify
from db.models.reddit_posts import RedditPost  # Import the RedditPost model
from db.models.youtube_posts import YoutubePost
from db.models.organization_table import OrganizationTable 

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

def get_reddit_data():
    try:
        posts = RedditPost.query.all()
        OrganizationTable
        like_count = 0
        comment_count = 0
        for post in posts:
            like_count = like_count + post.score
            comment_count =  comment_count + post.comms_num
        data = {'like_count': like_count, 'comment_count': comment_count}
        return jsonify(data)
    
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
    
def get_youtube_data():
    try:
        posts = YoutubePost.query.all()
        OrganizationTable
        like_count = 0
        comment_count = 0
        view_count = 0
        for post in posts:
            like_count = like_count + post.score
            comment_count =  comment_count + post.comms_num,
            view_count = 0
        data = {'like_count': like_count, 'comment_count': comment_count, 'view_count': view_count}
        return jsonify(data)
    
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
