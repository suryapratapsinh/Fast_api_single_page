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

#------------------------------------------------------------


# from sqlalchemy import create_engine
# from sqlalchemy.orm import sessionmaker, declarative_base

# # Use your actual URL here
# DATABASE_URL = "postgresql://postgres:Suraj_30112002@db.bqghunzqudzmsmnvnsvh.supabase.co:5432/postgres?sslmode=require"  #postgresql+psycopg2://postgres:Suraj_30112002@db.bqghunzqudzmsmnvnsvh.supabase.co:5432/postgres" 




# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(bind=engine, autocommit=False, autoflush=False)
# Base = declarative_base()

#------------------------------------------------------------

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

# 1. Get URL from environment variables
DATABASE_URL = os.getenv("DATABASE_URL")

# 2. Force SSL and correct driver format
if DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql+asyncpg://", 1)
    
if "sslmode" not in DATABASE_URL:
    DATABASE_URL += "?sslmode=require"

# 3. Async engine with connection pooling
engine = create_async_engine(
    DATABASE_URL,
    pool_pre_ping=True,  # Reconnects if DB drops
    pool_size=5,         # Enough for small traffic
    echo=True            # Debug only - disable later
)

# 4. Async session maker
SessionLocal = sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False
)

Base = declarative_base()







