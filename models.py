from sqlalchemy import Column, Integer, String, Float
from database import Base

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     name = Column(String(100))
#     age = Column(Integer)
#     contact = Column(String(20))
#     email = Column(String(100))
#     pr_10 = Column(Float)
#     pr_12 = Column(Float)
#     graduation_gpa = Column(Float)



class User(Base):
    __tablename__ = "users_info_table"

    id = Column(Integer, primary_key=True, index=True)
    Full_Name = Column(String(100))
    Email = Column(String(100))
    Phone = Column(String(20))
    Country_of_Interest = Column(String(20))
    Preferred_Intake = Column(String(20))
    Highest_Qualification = Column(String(30))
    IELTS_TOEFL_Score = Column(Float)
    Message = Column(String(200))

