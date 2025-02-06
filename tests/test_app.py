from http import HTTPStatus

from orion.app import database


def test_root_deveser_ok_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá mundo do FastApi! I Love You!'}


def test_create_user_deve_criar_usuario_e_return_201(client):
    response = client.post(
        '/users/',
        json={
            'username': 'teste',
            'email': 'test@exemplo.com',
            'password': '123456',
        },
    )

    assert database[0].id == 1
    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'username': 'teste',
        'email': 'test@exemplo.com',
        'id': 1,
    }


def test_read_users_deve_retornar_lista_de_users(client):
    response = client.get('/users/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [{'username': 'teste', 'email': 'test@exemplo.com', 'id': 1}]
    }


def test_update_user_retornar_200_e_user_atualizado(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'fulano',
            'email': 'fulano@exemplo.com',
            'password': 'xyz123',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fulano',
        'email': 'fulano@exemplo.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    # assert len([ x for x in database if x.id == 1]) <= 0
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
