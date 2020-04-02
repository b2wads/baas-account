from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from baas.api import app
from baas.models import Account
from baas.services.account import AccountService


class AccountAPITest(TestCase):
    async def setUp(self):
        AccountService.storage.clear()

    async def test_health(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/health")

            self.assertEqual(HTTPStatus.OK, resp.status)
            data = await resp.json()
            self.assertEqual({"OK": True}, data)

    async def test_salva_conta(self):
        async with HttpClientContext(app) as client:
            self.fail()

    async def test_lista_contas_banco_vazio(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/accounts")

            self.assertEqual(HTTPStatus.OK, resp.status)
            data = await resp.json()
            self.assertEqual([], data)

    async def test_lista_contas(self):
        acc = Account(nome="Dalton", cpf="42")
        async with HttpClientContext(app) as client:
            await client.post("/accounts", json=acc.dict())
            resp = await client.get("/accounts")

            self.assertEqual(HTTPStatus.OK, resp.status)
            data = await resp.json()

            self.assertEqual(1, len(data))
            acc_1 = Account(**data[0])
            self.assertEqual(acc_1, acc)
