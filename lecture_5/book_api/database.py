from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import sessionmaker

# string of db
SQLITE_DATABASE = "sqlite:///books.db"

# creating engine
engine = create_engine(SQLITE_DATABASE
                       ,connect_args={"check_same_thread": False})

# creating basic class
class Base(DeclarativeBase): pass

# creating a model
class Book(Base):
    __tablename__ = "books"
    book_id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    year = Column(Integer)

# session for connecting do database
SessionLocal = sessionmaker(autoflush=False, bind=engine)




