from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_user"

# Connect to DB
engine = create_engine(DATABASE_URL)
# engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# Create a session factory to talk to DB
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for models
Base = declarative_base()




