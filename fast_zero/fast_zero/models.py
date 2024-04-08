from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

# no ORM do SQLAlquemy, os modelos de estrutura dos dados são definidos como classes python
# que herdam de uma classe base comum, que é criada a partir de DeclarativeBase


class Base(DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    password: Mapped[str]
    email: Mapped[str]
    # Mapped é um atributo do python que é 'mapeado' a uma coluna específica em uma tabela de banco de dados
    # Esta abordagem permite ao SQLAlchemy realizar a conversão entre os tipos de dados
    # Python e os tipos de dados do banco de dados, além de oferecer uma interface Pythonica para a interação entre eles.
