from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./todosapp.db"
#SQLALCHEMY_DATABASE_URL = "postgresql:///postgres:password@localhost/db"
#QLALCHEMY_DATABASE_URL = "mysql+pymysql:///root:password@127.0.0.1:3306/db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) 
Base = declarative_base()

