# from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo(
    client,
):   # Arrange - configurando um lcient de testes para fazer a requisição ao app - resumido na função client
    response = client.get(
        '/'
    )   # Act - chamada do Sistema Sob teste: estamos exercitando a rota '/' e armazenando
    # a resposta na variável response - fase que executa o código a ser testado

    assert response.status_code == 200
    assert response.json() == {
        'message': 'Olá Mundo!'
    }   # Assert : verifica se tudo ocorreu como esperado
    #


# Teste para a rota POST deve verificar se a criação de um novo usuário funciona corretamente; enviamos um novo usuário
# para a rota /users/ e, em seguida, verifica a resposta é 201 (criado)


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )
    assert response.status_code == 201
    assert response.json() == {
        'username': 'alice',
        'email': 'alice@example.com',
        'id': 1,
    }


def test_read_user(client):
    response = client.get('/users/')
    assert response.status_code == 200   # success
    assert response.json() == {
        'users': [
            {
                'username': 'alice',
                'email': 'alice@example.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'bob',
            'email': 'bob@example.com',
            'password': 'mynewpass',
        },
    )
    assert response.status_code == 200
    assert response.json() == {
        'username': 'bob',
        'email': 'bob@example.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'message': 'User deleted'}
