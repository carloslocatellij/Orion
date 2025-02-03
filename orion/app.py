from http import HTTPStatus

from fastapi import FastAPI

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
