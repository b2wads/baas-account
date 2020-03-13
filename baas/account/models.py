from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str
    saldo: int = 10000


class Saque(BaseModel):
    data: Optional[str]
    valor: int


class Credito(BaseModel):
    data: Optional[str]
    valor: int
