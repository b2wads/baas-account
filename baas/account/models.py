from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int = 10000


class Saque(BaseModel):
    data: str
    valor: int


class Credito(BaseModel):
    data: str
    valor: int
