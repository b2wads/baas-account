from typing import List, Optional

from baas.models import Account, Debito, Credito


class AccountStorage:
    def __init__(self):
        self.clear()

    def clear(self):
        self.__data = dict()

    def save(self, acc_id: str, acc_data: Account) -> Account:
        self.__data[acc_id] = acc_data
        return acc_data

    def get_by_id(self, acc_id) -> Optional[Account]:
        return self.__data.get(acc_id)

    def list(self) -> List[Account]:
        return [acc[1] for acc in self.__data.items()]


class AccountService:

    storage = AccountStorage()

    @classmethod
    def save_account(cls, acc_id: str, acc_data: Account) -> Account:
        raise NotImplementedError

    @classmethod
    def get_by_id(cls, acc_id: str) -> Optional[Account]:
        raise NotImplementedError

    @classmethod
    def list(cls) -> List[Account]:
        raise NotImplementedError

    @classmethod
    def debita(cls, acc_id: str, debito: Debito) -> Optional[Account]:
        raise NotImplementedError

    @classmethod
    def credita(cls, acc_id: str, credito: Credito):
        raise NotImplementedError
