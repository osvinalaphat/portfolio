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
    template = Column(String)
    #NamePositionRight = Column(String)
    #NamePositionLeft = Column(String)
    #NamePositionUp = Column(String)
    #NamePositionDown = Column(String)
    #BiogPositionRight = Column(String)
    #BiogPositionLeft = Column(String)
    #BiogPositionUp = Column(String)
    #BiogPositionDown = Column(String)
    Box1Color = Column(String)
    Box2Color = Column(String)
    Box3Color = Column(String)
    Box4Color = Column(String)
    Box5Color = Column(String)
    Box6Color = Column(String)
    Box1Text = Column(String)
    Box2Text = Column(String)
    Box3Text = Column(String)
    Box4Text = Column(String)
    Box5Text = Column(String)
    Box6Text = Column(String)
    #Club1 = Column(String)
    #Club2 = Column(String)
    #Club3 = Column(String)
    #Club4 = Column(String)
    

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
    template: Optional[str]=None
    #NamePositionRight: Optional[str]=None
    #NamePositionLeft: Optional[str]=None
    #NamePositionUp: Optional[str]=None
    #NamePositionDown: Optional[str]=None
    #BiogPositionRight: Optional[str]=None
    #BiogPositionLeft: Optional[str]=None
    #BiogPositionUp: Optional[str]=None
    #BiogPositionDown: Optional[str]=None
    Box1Color: Optional[str]=None
    Box2Color: Optional[str]=None
    Box3Color: Optional[str]=None
    Box4Color: Optional[str]=None
    Box5Color: Optional[str]=None
    Box6Color: Optional[str]=None
    Box1Text: Optional[str]=None
    Box2Text: Optional[str]=None
    Box3Text: Optional[str]=None
    Box4Text: Optional[str]=None
    Box5Text: Optional[str]=None
    Box6Text: Optional[str]=None
    #Club1: Optional[str]=None
    #Club2: Optional[str]=None
    #Club3: Optional[str]=None
    #Club4: Optional[str]=None



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
            "name_color": user.name_color or "black",
            "biog_color": user.biog_color,
            "template": user.template,
            #"NamePositionRight":user.NamePositionRight,
            #"NamePositionLeft" : user.NamePositionLeft,
            #"NamePositionUp": user.NamePositionUp,
            #"NamePositionDown": user.NamePositionDown,
            #"BiogPositionRight": user.BiogPositionRight,
            #"BiogPositionLeft": user.BiogPositionLeft,
            #"BiogPositionUp": user.BiogPositionUp,
            #"BiogPositionDown": user.BiogPositionDown,
            "Box1Color": user.Box1Color,
            "Box2Color": user.Box2Color,
            "Box3Color": user.Box3Color,
            "Box4Color" : user.Box4Color,
            "Box5Color": user.Box5Color,
            "Box6Color": user.Box6Color,
            "Box1Text": user.Box1Text or "Box 1",
            "Box2Text": user.Box2Text or "Box 2",
            "Box3Text": user.Box3Text or "Box 3",
            "Box4Text": user.Box4Text or "Box 4",
            "Box5Text": user.Box5Text or "Box 5",
            "Box6Text": user.Box6Text or "Box 6",
            #"Club1":user.Club1,
            #"Club2":user.Club2,
            #"Club3":user.Club3,
            #"Club4":user.Club4,
        }
    else:
        # If user does not exist, return default values
        return {
            "title": "SLUH's page",
            "biog": "",
            "background_color": "",
            "name_color": "",
            "biog_color": "",
            "template": "",
            #"NamePositionRight":"",
            #"NamePositionLeft" : "",
            #"NamePositionUp": "",
            #"NamePositionDown":"",
            #"BiogPositionRight":"",
            #"BiogPositionLeft": "",
            #"BiogPositionUp": "",
            #"BiogPositionDown": "",
            "Box1Color": "",
            "Box2Color": "",
            "Box3Color": "",
            "Box4Color" : "",
            "Box5Color": "",
            "Box6Color": "",
            "Box1Text": "Box1",
            "Box2Text": "Box2",
            "Box3Text": "Box3",
            "Box4Text": "Box4",
            "Box5Text": "Box5",
            "Box6Text": "Box6",
            #"Club1":"",
            #"Club2":"",
            #"Club3":"",
            #"Club4":"",
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
    if user_post.biog_color is not None:
        user.biog_color = user_post.biog_color
    if user_post.template is not None:
        user.template = user_post.template
    #if user_post.NamePositionRight is not None:
    #    user.NamePositionRight = user_post.NamePositionRight
    #if user_post.NamePositionLeft is not None:
    #    user.NamePositionLeft = user_post.NamePositionLeft
    #if user_post.NamePositionUp is not None:
    #    user.NamePositionUp = user_post.NamePositionUp
    #if user_post.NamePositionDown is not None:
    #    user.NamePositionDown = user_post.NamePositionDown
    #if user_post.BiogPositionRight is not None:
    #    user.BiogPositionRight = user_post.BiogPositionRight
    #if user_post.BiogPositionLeft is not None:
    #    user.BiogPositionLeft = user_post.BiogPositionLeft
    #if user_post.BiogPositionUp is not None:
    #    user.BiogPositionUp = user_post.BiogPositionUp
    #if user_post.BiogPositionDown is not None:
    #    user.BiogPositionDown = user_post.BiogPositionDown
    if user_post.Box1Color is not None:
        user.Box1Color = user_post.Box1Color
    if user_post.Box2Color is not None:
        user.Box2Color = user_post.Box2Color
    if user_post.Box3Color is not None:
        user.Box3Color = user_post.Box3Color
    if user_post.Box4Color is not None:
        user.Box4Color = user_post.Box4Color
    if user_post.Box5Color is not None:
        user.Box5Color = user_post.Box5Color
    if user_post.Box6Color is not None:
        user.Box6Color = user_post.Box6Color
    if user_post.Box1Text is not None:
        user.Box1Text = user_post.Box1Text
    if user_post.Box2Text is not None:
        user.Box2Text = user_post.Box2Text
    if user_post.Box3Text is not None:
        user.Box3Text = user_post.Box3Text
    if user_post.Box4Text is not None:
        user.Box4Text = user_post.Box4Text
    if user_post.Box5Text is not None:
        user.Box5Text = user_post.Box5Text
    if user_post.Box6Text is not None:
        user.Box6Text = user_post.Box6Text
    #if user_post.Club1 is not None:
    #   user.Club1 = user_post.Club1
    #if user_post.Club2 is not None:
    #   user.Club2 = user_post.Club2
    #if user_post.Club3 is not None:
    #   user.Club3 = user_post.Club3
    #if user_post.Club4 is not None:
    #   user.Club4 = user_post.Club4
    
    db.commit()  # Commit changes to the database

    return {
        "title": f"{user.title}'s Portfolio",
        "biog": user.biog,
        "background_color": user.background_color,
        "name_color": user.name_color,
        "biog_color": user.biog_color,
        "template": user.template,
        #"NamePositionRight":user.NamePositionRight,
        #"NamePositionLeft" : user.NamePositionLeft,
        #"NamePositionUp": user.NamePositionUp,
        #"NamePositionDown": user.NamePositionDown,
        #"BiogPositionRight": user.BiogPositionRight,
        #"BiogPositionLeft": user.BiogPositionLeft,
        #"BiogPositionUp": user.BiogPositionUp,
        #"BiogPositionDown": user.BiogPositionDown,
        "Box1Color": user.Box1Color,
        "Box2Color": user.Box2Color,
        "Box3Color": user.Box3Color,
        "Box4Color" : user.Box4Color,
        "Box5Color": user.Box5Color,
        "Box6Color": user.Box6Color,
        "Box1Text": user.Box1Text,
        "Box2Text": user.Box2Text,
        "Box3Text": user.Box3Text,
        "Box4Text": user.Box4Text,
        "Box5Text": user.Box5Text,
        "Box6Text": user.Box6Text,
        #"Club1":user.Club1,
        #"Club2":user.Club2,
        #"Club3":user.Club3,
        #"Club4":user.Club4,
    }