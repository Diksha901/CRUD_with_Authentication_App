from .database import Base
from sqlalchemy import Column,Integer,String,ForeignKey
from sqlalchemy.orm import relationship
class Blog(Base):
    __tablename__='blogs'
    id=Column(Integer,primary_key=True,index=True)
    title=Column(String)
    body=Column(String)
    owner_id = Column(Integer, ForeignKey('users.id',ondelete="CASCADE"),nullable=False)
    owner=relationship('User',back_populates='blogs')

class User(Base):
    __tablename__='users'
    id=Column(Integer,primary_key=True,index=True)
    name=Column(String)
    email=Column(String)
    password=Column(String)
    blogs=relationship('Blog',back_populates='owner')

class Like(Base):
    __tablename__='likes'
    user_id=Column(Integer,ForeignKey("users.id",ondelete="CASCADE"),primary_key=True)
    blog_id=Column(Integer,ForeignKey("blogs.id",ondelete="CASCADE"),primary_key=True)