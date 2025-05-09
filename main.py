# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse, RedirectResponse
# from database import SessionLocal, engine
# from models import Base, User
#
# Base.metadata.create_all(bind=engine)
#
# app = FastAPI()
# templates = Jinja2Templates(directory="templates")
#
# @app.get("/", response_class=HTMLResponse)
# async def get_form(request: Request):
#     return templates.TemplateResponse("register.html", {"request": request})
#
# @app.post("/register")
# async def register_user(
#     request: Request,
#     name: str = Form(...),
#     age: int = Form(...),
#     contact: str = Form(...),
#     email: str = Form(...),
#     pr_10: float = Form(...),
#     pr_12: float = Form(...),
#     graduation_gpa: float = Form(...)
# ):
#     db = SessionLocal()
#     new_user = User(
#         name=name,
#         age=age,
#         contact=contact,
#         email=email,
#         pr_10=pr_10,
#         pr_12=pr_12,
#         graduation_gpa=graduation_gpa
#     )
#     db.add(new_user)
#     db.commit()
#     db.close()
#     return templates.TemplateResponse("register.html", {
#         "request": request,
#         "message": "Registration successful!"
#     })

#--------------------------------------------------------

# from fastapi import FastAPI, Request, Form
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from database import SessionLocal, engine
# from models import Base, User

# # Create tables in the database
# Base.metadata.create_all(bind=engine)

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# @app.get("/", response_class=HTMLResponse)
# async def get_form(request: Request):
#     return templates.TemplateResponse("register.html", {"request": request})

# @app.post("/register", response_class=HTMLResponse)
# async def register_user(
#     request: Request,
#     name: str = Form(...),
#     age: int = Form(...),
#     contact: str = Form(...),
#     email: str = Form(...),
#     pr_10: float = Form(...),
#     pr_12: float = Form(...),
#     graduation_gpa: float = Form(...)
#                                             ):

#     db = SessionLocal()
#     try:
#         new_user = User(
#             name=name,
#             age=age,
#             contact=contact,
#             email=email,
#             pr_10=pr_10,
#             pr_12=pr_12,
#             graduation_gpa=graduation_gpa
#         )
#         db.add(new_user)
#         db.commit()
#         message = "Registration successful!"
#     except Exception as e:
#         db.rollback()
#         print("❌ DB ERROR:", e)
#         message = f"Registration failed: {e}"
#     finally:
#         db.close()

#     return templates.TemplateResponse("register.html", {
#         "request": request,
#         "message": message
#     })

#--------------------------------------------------------------

# from fastapi import FastAPI, Request, Form, Depends
# from fastapi.templating import Jinja2Templates
# from fastapi.responses import HTMLResponse
# from sqlalchemy.ext.asyncio import AsyncSession
# from database import SessionLocal, engine, Base
# from models import User
# # from dotenv import load_dotenv
# import os
# import logging 

# # load_dotenv() 

# logging.basicConfig(level=logging.INFO)
# print("DATABASE_URL:", os.getenv("DATABASE_URL"))

# app = FastAPI()
# templates = Jinja2Templates(directory="templates")

# # Async DB initialization
# async def init_db():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)

# @app.on_event("startup")
# async def startup():
#     await init_db()

# # Dependency
# async def get_db():
#     async with SessionLocal() as session:
#         yield session

# # Routes (now async)
# @app.get("/", response_class=HTMLResponse)
# async def get_form(request: Request):
#     return templates.TemplateResponse("register.html", {"request": request})

# @app.post("/register", response_class=HTMLResponse)
# async def register_user(
#     request: Request,
#     name: str = Form(...),
#     age: int = Form(...),
#     contact: str = Form(...),
#     email: str = Form(...),
#     pr_10: float = Form(...),
#     pr_12: float = Form(...),
#     graduation_gpa: float = Form(...),
#     db: AsyncSession = Depends(get_db)  # Async session
# ):
#     try:
#         new_user = User(
#             name=name, age=age, contact=contact,
#             email=email, pr_10=pr_10, pr_12=pr_12,
#             graduation_gpa=graduation_gpa
#         )
#         db.add(new_user)
#         await db.commit()  # Async commit
#         message = "✅ Registration successful!"
#     except Exception as e:
#         await db.rollback()  # Async rollback
#         message = f"❌ Error: {str(e)}"
    
#     return templates.TemplateResponse("register.html", {
#         "request": request,
#         "message": message
#     })

#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++  latest

from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sqlalchemy.orm import Session
from database import SessionLocal, engine, Base
from models import User
import os

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Create tables on startup (sync)
@app.on_event("startup")
def startup_event():
    Base.metadata.create_all(bind=engine)

# Dependency for getting DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Routes
@app.get("/", response_class=HTMLResponse)
def get_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
def register_user(
     request: Request,
    Full_Name: str = Form(...),
    Email: str = Form(...),
    Phone: int = Form(...),
    Country_of_Interest: str = Form(...),
    Preferred_Intake: str = Form(...),
    Highest_Qualification: str = Form(...),
    IELTS_TOEFL_Score: str = Form(...),
    Message: str = Form(...),
    db:  Session = Depends(get_db)

):
    try:
        new_user = User(
            Full_Name=Full_Name,
            Email=Email,
            Phone=Phone,
            Country_of_Interest=Country_of_Interest,
            Preferred_Intake=Preferred_Intake,
            Highest_Qualification=Highest_Qualification,
            IELTS_TOEFL_Score = IELTS_TOEFL_Score,
            Message = Message
        )
        db.add(new_user)
        db.commit()
        db.close()

        
    except Exception as e:
        db.rollback()
        message = f"❌ Error: {str(e)}"

    return templates.TemplateResponse("success.html", {
        "request": request,
        "message": "✅ Registration successful!"
    })


