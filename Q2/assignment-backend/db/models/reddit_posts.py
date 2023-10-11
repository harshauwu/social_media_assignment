from app import db
from datetime import datetime
from typing import Any

class RedditPost(db.Model):
    __tablename__ = 'reddit_posts'

    # id = db.Column(db.String(255), primary_key=True)
    post_id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    comms_num = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    subreddit = db.Column(db.String(255), nullable=False)
    created_date = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    created_time = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    @staticmethod
    def create(title: str, post_id: str, score: int, id: str, url: str, comms_num: int, created: datetime, body: str, author: str,
               subreddit: str) -> "RedditPost":
        return RedditPost(
            title=title,
            post_id=post_id,
            score=score,
            id=id,
            url=url,
            comms_num=comms_num,
            created=created,
            body=body,
            author=author,
            subreddit=subreddit
        )

    def __str__(self) -> str:
        return f"<RedditPost {self.id}>"
