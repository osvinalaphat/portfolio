from fastapi import FastAPI,Request
from pydantic import BaseModel
from typing import Optional
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
#next is database stuff
from fastapi import Depends, HTTPException
from sqlalchemy.orm import Session #optional line of code
from sqlalchemy import Column, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
## to here



# Create database engine and session
engine = create_engine("sqlite:///./portfolio.db", connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

# Define the database model
class Portfolio(Base):
    __tablename__ = "portfolios"

    uid = Column(String, primary_key=True, index=True)
    title = Column(String)
    biog = Column(String)
    background_color = Column(String)
    name_color = Column(String)
    biog_color = Column(String)

# Create the tables in the database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
# Define the expected JSON structure

#####
##### to here is the database
#####

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # You can specify your frontend URL here
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

templates = Jinja2Templates(directory="templates")
app.mount("/static", StaticFiles(directory="static"), name="static")


class UserValidate(BaseModel):
    title : Optional[str] = None
    biog : Optional[str] = None
    background_color : Optional[str] = None
    name_color : Optional[str] = None
    biog_color : Optional[str] = None


@app.get("/")
async def front_image(request:Request):
    return templates.TemplateResponse("front.html", {"request": request})



@app.get("/my-page")
async def get_data(request: Request, db: Session = Depends(get_db)):
    uid = request.headers.get("Authorization")  # get UID from headers

    if not uid:
        raise HTTPException(status_code=400, detail="UID missing")

    # Query the database for the user's portfolio
    user = db.query(Portfolio).filter(Portfolio.uid == uid).first()

    if user:
        print("Returning name_color:", user.name_color)
        return {
            "title": f"{user.title}",
            "biog": user.biog,
            "background_color": user.background_color,
            "name_color": user.name_color or "white",
            "biog_color": user.biog_color,
        }
    else:
        # If user does not exist, return default values
        return {
            "title": "SLUH's page",
            "biog": "",
            "background_color": "",
            "name_color": "",
            "biog_color": ""
        }


@app.post("/my-page")
async def change_data(user_post: UserValidate, request: Request, db: Session = Depends(get_db)):
    uid = request.headers.get("Authorization")  # get UID from headers

    if not uid:
        raise HTTPException(status_code=400, detail="UID missing")

    # Check if user already exists in the database
    user = db.query(Portfolio).filter(Portfolio.uid == uid).first()

    if not user:
        # If user does not exist, create a new user record
        user = Portfolio(uid=uid, title="SLUH's page", biog="", background_color="", name_color="",biog_color="")
        db.add(user)
        db.commit()

    # Update the user's data with the new values
    if user_post.title is not None:
        user.title = user_post.title
    if user_post.biog is not None:
        user.biog = user_post.biog
    if user_post.background_color is not None:
        user.background_color = user_post.background_color
    if user_post.name_color is not None:
        user.name_color = user_post.name_color
        print("Saved name color:", user.name_color)

    if user_post.biog_color is not None:
        user.biog_color = user_post.biog_color

    db.commit()  # Commit changes to the database

    return {
        "title": f"{user.title}'s Portfolio",
        "biog": user.biog,
        "background_color": user.background_color,
        "name_color": user.name_color,
        "biog_color": user.biog_color,
    }