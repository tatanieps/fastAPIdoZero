from pydantic import BaseModel, EmailStr


class Message(BaseModel):
    message: str


class UserSchema(BaseModel):
    username: str
    email: EmailStr
    password: str


class UserPublic(
    BaseModel
):   # quando dava erro,tinha faltado incluir o id do usuario
    id: int
    username: str
    email: EmailStr


class UserDB(UserSchema):   # user, senha e id do user
    id: int


class UserList(BaseModel):
    users: list[UserPublic]
