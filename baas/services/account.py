from typing import List

from baas.account.models import Account, Saque


class AccountStorage:
    def __init__(self):
        self.__data = dict()

    def save(self, acc_id: str, acc_data: Account) -> Account:
        self.__data[acc_id] = acc_data
        return acc_data

    def get_by_id(self, acc_id) -> Account:
        return self.__data[acc_id]

    def list(self) -> List[Account]:
        return [acc[1] for acc in self.__data.items()]


class AccountService:

    storage = AccountStorage()

    @classmethod
    def save_account(cls, acc_id: str, acc_data: Account) -> Account:
        cls.storage.save(acc_id, acc_data)
        return acc_data

    @classmethod
    def get_by_id(cls, acc_id: str) -> Account:
        return cls.storage.get_by_id(acc_id)

    @classmethod
    def list(cls) -> List[Account]:
        return cls.storage.list()

    @classmethod
    def debita(cls, acc_id: str, saque: Saque):
        raise NotImplementedError
