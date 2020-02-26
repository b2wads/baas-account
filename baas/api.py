from typing import List

from aiohttp import web
from asyncworker import RouteTypes

from baas.account.models import Account, Saque, Credito
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
    return web.json_response(acc.dict())


@app.route(
    ["/accounts/{acc_id}/debito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
@parse_body(Saque)
async def debita_account(acc_id: str, saque: Saque) -> Saque:
    AccountService.debita(acc_id, saque)
    return web.json_response(saque.dict())


@app.route(
    ["/accounts/{acc_id}/credito"], type=RouteTypes.HTTP, methods=["POST"]
)
@parse_id(str)
async def credita_account(acc: Account) -> Credito:
    raise NotImplementedError


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health():
    return web.json_response({"OK": True})
