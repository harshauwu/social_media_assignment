from app import db
from datetime import datetime
from flask import jsonify
from db.models.schedule_posts import SchedulePost  # Import the SchedulePost model

def save_post(data):
    try:
        # Create a new SchedulePost object
        tags = data.get('tags')
        tags_str = ', '.join(tags) if tags else ''
        
        new_post = SchedulePost(
            title = data["title"],
            url = data["url"],
            body = data['text'],
            tags = tags_str,
            media = data['file'] if 'file' in data else '',
            is_one_time = data['is_one_time'],
            rule = data['rule'],
            status = 1,
            created_at = datetime.utcnow(),  # Use the current UTC time
            updated_at = datetime.utcnow(),  # Use the current UTC time
        )
        # Add the new_post to the session and commit it to the database
        db.session.add(new_post)
        db.session.commit()
        
        # Fetch the saved record by querying the database using the primary key
        saved_record = SchedulePost.query.get(new_post.id)

        # Return the saved record
        return saved_record

    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"
    
def get_all_schedule_posts():
    try:
        posts = SchedulePost.query.all()
        posts_data = []
        for post in posts:
            reddit_post_dict = {
                "id": post.id,
                "title": post.title,
                "body": post.body,
                "rule": post.rule,
                "tags": post.tags,
                "media" : post.media,
                "is_one_time" : post.is_one_time,
                "created_at": post.created_at
            }
            posts_data.append(reddit_post_dict)
        return posts_data
    except Exception as e:
        # Handle exceptions (e.g., database connection error)
        return f"Error fetching Reddit posts: {str(e)}"     

    


  


