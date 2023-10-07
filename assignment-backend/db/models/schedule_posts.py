from app import db
from datetime import datetime
from typing import Any

class SchedulePost(db.Model):
    __tablename__ = 'schedule_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    url = db.Column(db.String(255), nullable=False)
    body = db.Column(db.String(255))
    media = db.Column(db.String(255))  
    rule = db.Column(db.String(255))  
    tags = db.Column(db.String(255))  
    is_one_time = db.Column(db.Boolean)
    status = db.Column(db.Integer)
    created_at = db.Column(db.DateTime) 
    updated_at = db.Column(db.DateTime) 

    def __str__(self) -> str:
        return f"<SchedulePost id={self.id}, title='{self.title}'>"
    

    # def __str__(self):
    #     return self.name
