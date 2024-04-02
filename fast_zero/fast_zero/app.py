from fastapi import FastAPI, HTTPException

from fast_zero.schemas import Message, UserDB, UserList, UserPublic, UserSchema

app = FastAPI()

database = []


@app.get('/', status_code=200, response_model=Message)
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/users/', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_with_id)
    return user_with_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)  # user sem senha
def update_user(user_id: int, user: UserSchema):
    # if user_id not in database: - é possível usar a sintaxe, mas ela fica menos clara no código

    if user_id > len(database) or user_id < 0:
        raise HTTPException(status_code=404, detail='User not Found')

    user_with_id = UserDB(
        **user.model_dump(), id=user_id
    )   # o ** quer dizer que o dicionário será desempacotado em parâmetros
    # UserDB(username='nome do usuario', password='senha do usuario'), etc.
    database[user_id - 1] = user_with_id
    return user_with_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(status_code=404, detail='User not found')

    del database[user_id - 1]

    return {'message': 'User deleted'}
