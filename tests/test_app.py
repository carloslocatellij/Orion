from http import HTTPStatus

from fastapi.testclient import TestClient

from orion.app import app


def test_root_deveser_ok_e_ola_mundo():
    client = TestClient(app)
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'message': 'Olá mundo do FastApi! \n I Love You!'
    }
