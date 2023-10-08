from app import db
from datetime import datetime
from typing import Any

class RedditPostComment(db.Model):
    __tablename__ = 'reddit_post_comments'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String)
    post_author = db.Column(db.String)
    comment_auther = db.Column(db.String)
    comment_id = db.Column(db.String)
    comment_body = db.Column(db.String)
    comment_score = db.Column(db.BigInteger)
    comment_created_utc = db.Column(db.Float)
    comment_permalink = db.Column(db.String)
    is_root_comment = db.Column(db.Boolean)
    comment_author_flair_text = db.Column(db.String)
    process_comment_body = db.Column(db.String)
    sentiment_scores = db.Column(db.String)
    compound_sentiment = db.Column(db.Float)
    sentiment = db.Column(db.String)

    def __str__(self) -> str:
        return f"<RedditPostComment {self.id}>"