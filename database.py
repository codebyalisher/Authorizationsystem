from sqlalchemy import create_engine, MetaData
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from databases import Database

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL)
metadata = MetaData()
Base = declarative_base(metadata=metadata)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
database = Database(DATABASE_URL)
