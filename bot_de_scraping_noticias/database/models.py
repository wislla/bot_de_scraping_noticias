from sqlalchemy import create_engine, Column, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class NewsArticle(Base):
    __tablename__ = 'news_articles'
    id = Column(String, primary_key=True)
    headline = Column(String)


def get_engine():
    return create_engine('sqlite:///news.db')


def get_session():
    engine = get_engine()
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return Session()
