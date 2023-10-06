from app import db
from datetime import datetime
from typing import Any

class OrganizationTable(db.Model):
    __tablename__ = 'organization_table'

    id = db.Column(db.String(255), primary_key=True)
    social_media_platform = db.Column(db.String(255), primary_key=True)
    description = db.Column(db.String(255), nullable=False)
    display_name = db.Column(db.Integer, nullable=False)
    image = db.Column(db.String(255), nullable=False)
    subscribers = db.Column(db.Integer, nullable=False)
    title = db.Column(db.Text, nullable=False)
    url = db.Column(db.String(255), nullable=False)

    def __str__(self) -> str:
        return f"<OrganizationTable {self.id}>"
