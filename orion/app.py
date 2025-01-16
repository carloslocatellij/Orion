from http import HTTPStatus
from fastapi import FastAPI
from orion.schemas import *

app = FastAPI()


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Olá mundo do FastApi! \n I Love You!'}
