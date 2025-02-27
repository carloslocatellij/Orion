from http import HTTPStatus

from fastapi import FastAPI, HTTPException

from orion.schemas import Message, User, UserDB, UserList, UserPublic

app = FastAPI()

database = []


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo do FastApi! I Love You!'}


@app.post('/users/', status_code=HTTPStatus.CREATED, response_model=UserPublic)
def create_user(user: User):
    user_id = UserDB(**user.model_dump(), id=len(database) + 1)
    database.append(user_id)

    return user_id


@app.get('/users/', response_model=UserList)
def read_users():
    return {'users': database}


@app.put('/users/{user_id}', response_model=UserPublic)
def update_user(user_id: int, user: User, status_code=HTTPStatus.OK):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    user_id = UserDB(**user.model_dump(), id=user_id)

    return user_id


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(user_id: int):
    if user_id > len(database) or user_id < 1:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND, detail='User not found'
        )
    del database[user_id - 1]

    return {'message': 'User deleted'}
