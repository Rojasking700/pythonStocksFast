from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from database import get_db, Base, engine
from models import User
from pydantic import BaseModel

app = FastAPI()

# Create tables
Base.metadata.create_all(bind=engine)

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/")
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    db_user = User(name=user.name, email=user.email)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@app.get("/users/")
def read_users(db: Session = Depends(get_db)):
    return db.query(User).all()
