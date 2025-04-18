# import os
# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# DATABASE_URL = os.getenv("DATABASE_URL")  # pulls from ENV vars
# # DATABASE_URL = "mysql+pymysql://root:@localhost/fastapi_user"

# # Connect to DB
# engine = create_engine(DATABASE_URL)
# # engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# # Create a session factory to talk to DB
# # SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# # SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)


# # Base class for models
# Base = declarative_base()


# DATABASE_URL = os.getenv("DATABASE_URL")  # pulls from ENV vars




from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# Use your actual URL here
DATABASE_URL = "postgresql://postgres:Suraj_30112002@db.bqghunzqudzmsmnvnsvh.supabase.co:5432/postgres?sslmode=require"  #postgresql+psycopg2://postgres:Suraj_30112002@db.bqghunzqudzmsmnvnsvh.supabase.co:5432/postgres" 




engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
Base = declarative_base()







