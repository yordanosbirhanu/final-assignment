from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import models
from datetime import date

models.Base.metadata.create_all(bind=engine)
app = FastAPI(title="Library Management CRUD API")

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Create a new member
@app.post("/members/")
def create_member(fullname: str, email: str, join_date: str = date.today(), db: Session = Depends(get_db)):
    new_member = models.Member(FullName=fullname, Email=email, JoinDate=join_date)
    db.add(new_member)
    db.commit()
    db.refresh(new_member)
    return new_member

# Get all members
@app.get("/members/")
def read_members(db: Session = Depends(get_db)):
    return db.query(models.Member).all()

# Create a new book
@app.post("/books/")
def create_book(title: str, isbn: str, published_year: int, db: Session = Depends(get_db)):
    new_book = models.Book(Title=title, ISBN=isbn, PublishedYear=published_year)
    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    return new_book

# Get all books
@app.get("/books/")
def read_books(db: Session = Depends(get_db)):
    return db.query(models.Book).all()
