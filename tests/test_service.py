from asynctest import TestCase

from baas.account.models import Account
from baas.services.account import AccountService


class ServiceTest(TestCase):
    async def test_list_accounts(self):
        acc = Account(nome="Dalton Barreto", cpf="1234", saldo=1000)
        acc_2 = Account(nome="Dalton Barreto 2", cpf="4321", saldo=1000)
        AccountService.save_account(acc.cpf, acc)
        AccountService.save_account(acc_2.cpf, acc_2)
        self.assertEqual([acc, acc_2], AccountService.list())
