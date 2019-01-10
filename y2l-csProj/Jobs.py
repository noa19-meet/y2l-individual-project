from model import Base,Post
from post import *

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


engine = create_engine('sqlite:///lecture.db')
Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)
session = DBSession()
def query_by_give():
	posts = session.query(Post).filter_by(category="give").all()
	return posts

