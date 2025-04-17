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



from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from database import SessionLocal, engine
from models import Base, User

# Create tables in the database
Base.metadata.create_all(bind=engine)

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_form(request: Request):
    return templates.TemplateResponse("register.html", {"request": request})

@app.post("/register", response_class=HTMLResponse)
async def register_user(
    request: Request,
    name: str = Form(...),
    age: int = Form(...),
    contact: str = Form(...),
    email: str = Form(...),
    pr_10: float = Form(...),
    pr_12: float = Form(...),
    graduation_gpa: float = Form(...)
                                            ):

    db = SessionLocal()
    try:
        new_user = User(
            name=name,
            age=age,
            contact=contact,
            email=email,
            pr_10=pr_10,
            pr_12=pr_12,
            graduation_gpa=graduation_gpa
        )
        db.add(new_user)
        db.commit()
        message = "Registration successful!"
    except Exception as e:
        db.rollback()
        print("❌ DB ERROR:", e)
        message = f"Registration failed: {e}"
    finally:
        db.close()

    return templates.TemplateResponse("register.html", {
        "request": request,
        "message": message
    })
