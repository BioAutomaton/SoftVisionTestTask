from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .database import Base

UserGame = Table(
    'UserGame',
    Base.metadata,
    Column('user_id', ForeignKey('users.id'), primary_key=True),
    Column('game_id', ForeignKey('games.id'), primary_key=True)
)


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    age = Column(Integer)
    name = Column(String(120))
    email = Column(String, unique=True, index=True)

    games = relationship('Game', secondary=UserGame, back_populates='users')


class Game(Base):
    __tablename__ = 'games'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(120))

    users = relationship('User', secondary=UserGame, back_populates='games')
