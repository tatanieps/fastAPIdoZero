from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app) # Arrange - configurando um lcient de testes para fazer a requisição ao app

    response = client.get('/') # Act - chamada do Sistema Sob teste: estamos exercitando a rota '/' e armazenando
    #a resposta na variável response - fase que executa o código a ser testado

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'} # Assert : verifica se tudo ocorreu como esperado
    #


