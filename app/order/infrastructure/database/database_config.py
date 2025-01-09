from sqlalchemy import create_engine, text
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv
from decouple import config

load_dotenv()

SQLALCHEMY_DATABASE_URL = 'postgresql://%(db_user)s:%(db_passwd)s@%(db_host)s:%(db_port)s/%(db_name)s?client_encoding=utf8' % {
    "db_user": config("POSTGRES_USER"),
    "db_passwd": config("POSTGRES_PASSWORD"),
    "db_host": config("POSTGRES_HOST"),
    "db_port": config("POSTGRES_PORT"),
    "db_name": config("POSTGRES_DB"),
}

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def test_connection():
    with engine.connect() as connection:
        result = connection.execute(text("SELECT 1"))
        return result.scalar()


if test_connection() == 1:
        print("Connection successful!")
else:
        print("Connection failed.")