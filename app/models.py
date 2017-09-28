from datetime import datetime

from app import db


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.String(100), nullable=False, primary_key=True)
    created = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)
    updated = db.Column(db.DateTime, default=datetime.utcnow, nullable=False,
                        onupdate=datetime.utcnow)
    name = db.Column(db.String(100), nullable=False)
    profile_url = db.Column(db.String(200), nullable=False)
    access_token = db.Column(db.String(100), nullable=False)
