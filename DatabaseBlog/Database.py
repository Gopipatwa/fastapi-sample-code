from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# enigne = create_engine('sqlite://:memory',echo=True)
# enigne = create_engine('sqlite://./blog.db',echo=True)


SQLALCHAMY_DATABASE_URL = "sqlite:///./blog.db" 

enigne = create_engine(SQLALCHAMY_DATABASE_URL,connect_args={"check_same_thread":False})

SessionLocal = sessionmaker(bind=enigne,autocommit=False,autoflush=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()