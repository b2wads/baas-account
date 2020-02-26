from asynctest import TestCase, mock

from baas.account.models import Account
from baas.services.account import AccountService, AccountStorage


class ServiceTest(TestCase):
    async def test_list_accounts(self):
        storage = AccountStorage()
        with mock.patch.object(AccountService, "storage", storage):
            acc = Account(nome="Dalton Barreto", cpf="1234", saldo=1000)
            acc_2 = Account(nome="Dalton Barreto 2", cpf="4321", saldo=1000)

            storage.save(acc.cpf, acc)
            storage.save(acc_2.cpf, acc_2)

            self.assertEqual([acc, acc_2], AccountService.list())
