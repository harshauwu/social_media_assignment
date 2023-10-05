from app import db
from datetime import datetime
from typing import Any

class YoutubePost(db.Model):
    __tablename__ = 'youtube_posts'

    id = db.Column(db.String(255), primary_key=True)
    post_id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    score = db.Column(db.Integer, nullable=False)
    url = db.Column(db.String(255), nullable=False)
    comms_num = db.Column(db.Integer, nullable=False)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(255), nullable=False)
    subreddit = db.Column(db.String(255), nullable=False)

    def __str__(self) -> str:
        return f"<YoutubePost {self.id}>"
