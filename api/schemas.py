from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    name: str
    age: int

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    name: str

    class Config:
        orm_mode = True


class Game(GameBase):
    id: int


class User(UserBase):
    id: int


class UserGameConnectionSchema(BaseModel):
    game_id: int
    user_id: int


class GameSchema(Game):
    users: list[User]


class UserSchema(User):
    games: list[Game]
