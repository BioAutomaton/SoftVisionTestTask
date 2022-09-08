from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_game(db: Session, game_id: int):
    return db.query(models.Game).filter(models.Game.id == game_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserBase):
    db_user = models.User(email=user.email, name=user.name, age=user.age)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def create_game(db: Session, game: schemas.GameBase):
    db_game = models.Game(name=game.name)
    db.add(db_game)
    db.commit()
    db.refresh(db_game)
    return db_game


def get_games(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Game).offset(skip).limit(limit).all()


def connect_user_to_game(db: Session, game_id: int, user_id: int):
    db_game = db.query(models.Game).filter(models.Game.id == game_id).first()
    db_user = db.query(models.User).filter(models.User.id == user_id).first()

    if db_game and db_user:
        db_user_game_conn = db.query(models.UserGameConnection).filter(
            models.UserGameConnection.c.user_id == db_user.id,
            models.UserGameConnection.c.game_id == db_game.id).first()

        if db_user_game_conn is None:
            db_game.users.append(db_user)
            db.commit()
            db.refresh(db_game)
            db.refresh(db_user)

            db_user_game_conn = db.query(models.UserGameConnection).filter(
                models.UserGameConnection.c.user_id == db_user.id,
                models.UserGameConnection.c.game_id == db_game.id).first()
        return db_user_game_conn

    return None
