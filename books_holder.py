from sqlalchemy import create_engine, Column, Intiger, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.types import Numeric


engine = create_engine("sqlite:///books.db", echo=True)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()


class Books(Base):
    __tablename__ = 'Books'

    id = Column(Intiger ,primary_key=True)
    author = Column(String)
    published = Column(Date)
    price = Column(Numeric(10, 2))
    
    def __repr__(self):
        return f'<Title: {self.author} Published: {self.published} Price: {self.price}>'
