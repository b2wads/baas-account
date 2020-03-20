from asynctest import TestCase

from baas.models import Account
from baas.services.account import AccountStorage


class AccountStorageTest(TestCase):
    async def setUp(self):
        self.storage = AccountStorage()

    async def test_clear_storage(self):
        acc = Account(nome="Dalton Barreto", cpf="42")
        self.storage.save(acc.cpf, acc)

        self.assertEqual(acc.dict(), self.storage.get_by_id(acc.cpf))
        self.storage.clear()

        self.assertEqual(None, self.storage.get_by_id(acc.cpf))

    async def test_list(self):
        acc = Account(nome="Dalton Barreto", cpf="42")
        self.storage.save(acc.cpf, acc)

        self.assertEqual([acc], self.storage.list())
