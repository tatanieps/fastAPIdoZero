# O arquivo conftest.py é um arquivo especial reconhecido pelo pytest que permite definir fixtures que podem ser
# reutilizadas em diferentes módulos de teste em um projeto. É uma forma de centralizar recursos comuns de teste.

import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fast_zero.app import app
from fast_zero.models import Base

# Agora, em vez de repetir a criação do client em cada teste, podemos simplesmente passar a fixture
# como um argumento nos nossos testes:


@pytest.fixture
def client():
    return TestClient(app)


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:'
    )   # sqlite como db criado em memória
    Session = sessionmaker(
        bind=engine
    )   # fabrica de sessoes para sessoes de teste
    Base.metadata.create_all(
        engine
    )   # cria as tabelas no db antes de cada teste q use a fixture
    yield Session()   # cria uma instancia de session q será usada em cada teste q solicita a fixture - vai interagir com o banco de dados teste
    Base.metadata.drop_all(
        engine
    )   # após cada teste, as tabelas são excluídas


# teste unitário: cada tste vai ser isolado, em ambiente proprio
