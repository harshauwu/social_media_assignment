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
        like_count = 0
        comment_count = 0

        posts = RedditPost.query.all()
        reddit = OrganizationTable.query.filter_by(social_media_platform='Reddit').first()
        subscribers = reddit.subscribers
       
        for post in posts:
            like_count = like_count + post.score
            comment_count =  comment_count + post.comms_num

        data = {'like_count': like_count, 'comment_count': comment_count, 'subscriber_count': subscribers}

        return jsonify(data)
    
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
        return jsonify(data)
    
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
