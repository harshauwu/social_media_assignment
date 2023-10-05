from app import db
from datetime import datetime
from typing import Any

class SchedulePost(db.Model):
    __tablename__ = 'schedule_posts'

    id = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    body = db.Column(db.Text, nullable=False)
    media = db.Column(db.Text)  
    post_at = db.Column(db.DateTime)  
    tags = db.Column(db.String(255))  
    created_at = db.Column(db.DateTime) 
    updated_at = db.Column(db.DateTime) 

    def __str__(self) -> str:
        return f"<SchedulePost id={self.id}, title='{self.title}'>"
    

    # def __str__(self):
    #     return self.name
