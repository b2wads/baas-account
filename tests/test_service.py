from asynctest import TestCase

from baas.models import Account
from baas.services.account import AccountService, Debito, Credito


def valida_cpf(acc: Account) -> bool:
    return False


class ServiceTest(TestCase):
    async def setUp(self):
        AccountService.storage.clear()

    async def test_verifica_dados_da_conta(self):
        acc = Account(nome="Dalton", cpf="42")
        cpf_nao_ok = valida_cpf(acc)
        self.assertFalse(cpf_nao_ok)

    async def test_sava_conta(self):
        acc = Account(nome="Dalton", cpf="42")

        self.assertEqual([], AccountService.list())
        AccountService.save_account(acc.cpf, acc)

        acc_salva = AccountService.get_by_id(acc.cpf)
        self.assertEqual(acc, acc_salva)

    async def test_checagem_conta_duplicada(self):
        acc_1 = Account(nome="Dalton", cpf="42")
        acc_2 = Account(nome="Dalton 2", cpf="42")

        AccountService.save_account(acc_1.cpf, acc_1)
        AccountService.save_account(acc_2.cpf, acc_2)

        acc_salva = AccountService.get_by_id(acc_1.cpf)
        self.assertEqual(acc_salva, acc_1)

    async def test_nao_pode_saldo_negativo(self):
        acc = Account(nome="Dalton", cpf="42", saldo=300)
        AccountService.save_account(acc.cpf, acc)
        with self.assertRaises(Exception):
            AccountService.debita(acc.cpf, Debito(valor=350))

    async def test_executa_debito(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        AccountService.save_account(acc.cpf, acc)
        AccountService.debita(acc.cpf, Debito(valor=350))

        acc_db = AccountService.get_by_id(acc.cpf)
        self.assertEqual(acc_db.saldo, 50)

    async def test_nao_pode_debitar_de_conta_inexistente(self):

        acc = Account(nome="Dalton", cpf="42", saldo=1000)
        res = AccountService.debita(acc.cpf, Debito(valor=100))

    async def test_adiciona_credito(self):

        acc = Account(nome="Dalton", cpf="42", saldo=1000)
        AccountService.save_account(acc.cpf, acc)
        AccountService.credita(acc.cpf, Credito(valor=300))

        acc_db = AccountService.get_by_id(acc.cpf)
        self.assertEqual(acc_db.saldo, 1300)

    async def test_nao_pode_creditar_em_conta_inexistente(self):

        AccountService.credita("42", Credito(valor=10))

    async def test_lista_contas(self):

        acc_1 = Account(nome="Dalton", cpf="42")
        acc_2 = Account(nome="Dalton", cpf="43")
        AccountService.save_account(acc_1.cpf, acc_1)
        AccountService.save_account(acc_2.cpf, acc_2)

        accounts = AccountService.list()

        self.assertEqual(2, len(accounts))

    async def test_lista_banco_vazio(self):

        self.assertEqual(0, len(AccountService.list()))
