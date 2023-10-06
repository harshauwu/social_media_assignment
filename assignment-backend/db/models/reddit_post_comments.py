from app import db
from datetime import datetime
from typing import Any

class RedditPostComment(db.Model):
    __tablename__ = 'reddit_post_comments'
    
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.String(255))
    post_author = db.Column(db.String(255))
    comment_auther = db.Column(db.String(255))
    comment_id = db.Column(db.String(255))
    comment_body = db.Column(db.String(255))
    comment_score = db.Column(db.Integer)
    comment_created_utc = db.Column(db.DateTime)
    comment_permalink = db.Column(db.String(255))
    is_root_comment = db.Column(db.String(255))
    comment_author_flair_text = db.Column(db.String(255))
    process_comment_body = db.Column(db.String(255))
    sentiment_scores = db.Column(db.String(255))
    compound_sentiment = db.Column(db.Float)
    sentiment = db.Column(db.String(255))

    def __str__(self) -> str:
        return f"<RedditPostComment {self.id}>"

    # def group_by_sentiment():
    #     sentiment_counts = db.session.query(
    #         RedditPostComment.sentiment,
    #         func.count(RedditPostComment.id).label('count')
    #     ).group_by(RedditPostComment.sentiment).all()

    #     # 'sentiment_counts' will contain a list of tuples (sentiment, count)
        
    #     return sentiment_counts