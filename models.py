from sqlalchemy import Column, Integer, String, Float
from database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    age = Column(Integer)
    contact = Column(String(20))
    email = Column(String(100))
    pr_10 = Column(Float)
    pr_12 = Column(Float)
    graduation_gpa = Column(Float)
