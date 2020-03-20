from typing import List

from aiohttp import web
from asyncworker.http.decorators import parse_path

from baas.app import app
from baas.http import parse_body
from baas.models import Account, Debito, Credito
from baas.services.account import AccountService


@app.http(["/accounts"], methods=["POST"])
@parse_body(Account)
async def create_account(acc: Account) -> Account:
    acc = AccountService.save_account(acc.cpf, acc)
    return web.json_response(acc.dict())


@app.http(["/accounts"])
async def list_accounts() -> List[Account]:
    acc_list = AccountService.list()
    return web.json_response([acc.dict() for acc in acc_list])


@app.http(["/accounts/{acc_id}"])
@parse_path
async def get_by_id(acc_id: str) -> Account:
    acc = AccountService.get_by_id(acc_id)
    if acc:
        return web.json_response(acc.dict())
    else:
        return web.json_response(None)


@app.http(["/accounts/{acc_id}/debito"], methods=["POST"])
@parse_body(Debito)
@parse_path
async def debita_account(acc_id: str, debito: Debito) -> Debito:
    AccountService.debita(acc_id, debito)
    return web.json_response(debito.dict())


@app.http(["/accounts/{acc_id}/credito"], methods=["POST"])
@parse_path
@parse_body(Credito)
async def credita_account(acc_id: str, credito: Credito) -> Credito:
    AccountService.credita(acc_id, credito)
    return web.json_response(credito.dict())


@app.http(["/health"])
async def health():
    return web.json_response({"OK": True})
