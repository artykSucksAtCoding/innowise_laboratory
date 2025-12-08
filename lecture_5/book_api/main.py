from database import *
from sqlalchemy.orm import Session
from fastapi import Depends, FastAPI, Body
from fastapi.responses import JSONResponse, FileResponse
from fastapi import Query

from pydantic import BaseModel
from typing import Optional

class BookCreate(BaseModel):
    title: str
    author: str
    year: Optional[int] = None

class BookUpdate(BaseModel):
    title: Optional[str] = None
    author: Optional[str] = None
    year: Optional[int] = None

# creating app
app = FastAPI()

@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

@app.get("/")
def root():
    return {"message": "Hello, API is alive!"}

# creating dependencies
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# adding a book
@app.post("/books")
def create_book(data: BookCreate, db: Session = Depends(get_db)):
    book = Book(
        title=data.title,
        author=data.author,
        year=data.year
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book



# getting all the books
@app.get("/books")
def get_books(db: Session = Depends(get_db)):
    return db.query(Book).all()

# deleting  the book
@app.delete("/books/{book_id}")
def delete_book(book_id: int, db: Session = Depends(get_db)):

    # find book by id
    book = db.query(Book).filter(Book.book_id == book_id).first()

    # if not found throw an error window
    if book is None:
        return JSONResponse(status_code=404, content={"message": "Book not found"})

    db.delete(book)  # delete if in db
    db.commit()  # saving changes
    return book

# edit book
@app.put("/books/{book_id}")
def edit_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):

    # get a book by id
    book = db.query(Book).filter(Book.book_id == book_id).first()

    # if not found, send an error message
    if book == None:
        return JSONResponse(status_code=404, content={"message": "Book not found"})

    # changing values
    if data.title is not None:
        book.title = data.title
    if data.author is not None:
        book.author = data.author
    if data.year is not None:
        book.year = data.year

    db.commit()  # saving changes
    db.refresh(book)
    return book


@app.get("/books/search")
def search_books(
    title: str | None = Query(None, description="Name of a book"),
    author: str | None = Query(None, description="Author of a book"),
    year: int | None = Query(None, description="Year of a book"),
    db: Session = Depends(get_db)
):
    query = db.query(Book)

    if title:
        query = query.filter(Book.title.ilike(f"%{title}%"))
    if author:
        query = query.filter(Book.author.ilike(f"%{author}%"))
    if year:
        query = query.filter(Book.year == year)

    return query.all()



