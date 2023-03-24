from databases import Database
from sqlalchemy import create_engine, MetaData
from core.config import DATABASE_URL
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os
os.environ["SQLALCHEMY_WARN_20"] = "1"

database = Database(DATABASE_URL)
metadata = MetaData()
engine = create_engine(
    DATABASE_URL,
)

Session = sessionmaker(bind=engine)
session = Session()

