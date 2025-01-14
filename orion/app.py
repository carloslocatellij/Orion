from fastapi import FastAPI

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá mundo do FastApi! \n I Love You!'}
