from sqlalchemy import Column, Integer, String, Date, ForeignKey
from database import Base

class Member(Base):
    __tablename__ = "Members"
    MemberID = Column(Integer, primary_key=True, index=True)
    FullName = Column(String(100), nullable=False)
    Email = Column(String(100), unique=True, nullable=False)
    JoinDate = Column(Date, nullable=False)

class Book(Base):
    __tablename__ = "Books"
    BookID = Column(Integer, primary_key=True, index=True)
    Title = Column(String(200), nullable=False)
    ISBN = Column(String(20), unique=True, nullable=False)
    PublishedYear = Column(Integer)
