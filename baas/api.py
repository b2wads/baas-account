from typing import List

from aiohttp import web
from asyncworker import RouteTypes

from baas.account.models import Account, Debito, Credito
from baas.app import app
from baas.http import parse_body, parse_id
from baas.services.account import AccountService


@app.route(["/accounts"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Account)
async def create_account(acc: Account) -> Account:
    acc = AccountService.save_account(acc.cpf, acc)
    return web.json_response(acc.dict())


@app.route(["/accounts"], type=RouteTypes.HTTP, methods=["GET"])
async def list_accounts() -> List[Account]:
    acc_list = AccountService.list()
    return web.json_response([acc.dict() for acc in acc_list])


@app.route(["/accounts/{acc_id}"], type=RouteTypes.HTTP, methods=["GET"])
@parse_id(str)
async def get_by_id(acc_id: str) -> Account:
    acc = AccountService.get_by_id(acc_id)
    if acc:
        return web.json_response(acc.dict())
    else:
        return web.json_response(None)


@app.route(
    ["/accounts/{acc_id}/debito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
@parse_body(Debito)
async def debita_account(acc_id: str, debito: Debito) -> Debito:
    AccountService.debita(acc_id, debito)
    return web.json_response(debito.dict())


@app.route(
    ["/accounts/{acc_id}/credito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
@parse_body(Credito)
async def credita_account(acc_id: str, credito: Credito) -> Credito:
    AccountService.credita(acc_id, credito)
    return web.json_response(credito.dict())


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health():
    return web.json_response({"OK": True})
