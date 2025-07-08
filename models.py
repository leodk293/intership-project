# models.py
from sqlalchemy import create_engine, Column, Integer, String, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()

class SocialPost(Base):
    __tablename__ = 'social_posts'
    id = Column(Integer, primary_key=True)
    content = Column(Text)
    platform = Column(String(50))
    scheduled_time = Column(DateTime)
    status = Column(String(20))
    engagement_metrics = Column(Text)

class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    sender = Column(String(255))
    subject = Column(String(500))
    body = Column(Text)
    category = Column(String(100))
    priority = Column(String(20))
    response_generated = Column(Text)