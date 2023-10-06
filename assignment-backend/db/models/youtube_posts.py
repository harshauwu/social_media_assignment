from app import db
from datetime import datetime
from typing import Any

class YoutubePost(db.Model):
    __tablename__ = 'youtube_posts'

    id = db.Column(db.String(255), primary_key=True)
    view_count = db.Column(db.String(255), primary_key=True)
    comment_count = db.Column(db.String(255), nullable=False)
    duration = db.Column(db.Integer, nullable=False)
    published_at = db.Column(db.String(255), nullable=False)
    published_date = db.Column(db.Integer, nullable=False)
    published_time = db.Column(db.Text, nullable=False)

    def __str__(self) -> str:
        return f"<YoutubePost {self.id}>"
