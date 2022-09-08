from typing import List

from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session

from api.database import engine, SessionLocal
from . import crud, models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/users/", response_model=schemas.UserSchema)
def create_user(user: schemas.UserBase, db: Session = Depends(get_db)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    if not (0 <= user.age <= 100):
        raise HTTPException(status_code=400, detail="Age must be in range 0-100")

    return crud.create_user(db=db, user=user)


@app.post("/games/", response_model=schemas.GameSchema)
def create_game(game: schemas.GameBase, db: Session = Depends(get_db)):
    return crud.create_game(db=db, game=game)


@app.get("/users/", response_model=List[schemas.UserSchema])
def read_users(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    users = crud.get_users(db, skip=skip, limit=limit)
    return users


@app.post("/games/{game_id}/connect/{user_id}", response_model=schemas.UserGameConnectionSchema)
def connect_user_to_game(game_id: int, user_id: int, db: Session = Depends(get_db)):
    connection = crud.connect_user_to_game(db=db, game_id=game_id, user_id=user_id)
    if connection:
        return connection
    else:
        raise HTTPException(status_code=400, detail="User or game not found")


@app.get("/games/", response_model=List[schemas.GameSchema])
def read_games(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    games = crud.get_games(db, skip=skip, limit=limit)
    return games


@app.get("/users/{user_id}", response_model=schemas.UserSchema)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user


@app.get("/users/{game_id}", response_model=schemas.GameSchema)
def read_game(game_id: int, db: Session = Depends(get_db)):
    db_game = crud.get_game(db, game_id=game_id)
    if db_game is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_game
