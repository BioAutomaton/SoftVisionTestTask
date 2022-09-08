from pydantic import BaseModel


class UserBase(BaseModel):
    id: int
    email: str
    name: str
    age: int

    class Config:
        orm_mode = True


class GameBase(BaseModel):
    id: int
    name: str

    class Config:
        orm_mode = True


class UserSchema(UserBase):
    games: list[GameBase]


class GameSchema(GameBase):
    users: list[UserBase]


class UserCreate(UserBase):
    pass


class GameCreate(GameBase):
    pass
