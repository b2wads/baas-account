from functools import wraps
from typing import get_type_hints, List, Type

from aiohttp import web
from asyncworker import App, RouteTypes
from asyncworker.http.wrapper import RequestWrapper
from asyncworker.routes import call_http_handler


class MyApp(App):
    def http(self, routes: List[str], methods: List[str] = ["GET"]):
        def _wrap(handler):
            return self.route(routes, type=RouteTypes.HTTP, methods=methods)(
                self._unwrap_pydantic_model(handler)
            )

        return _wrap

    def _unwrap_pydantic_model(self, handler):
        async def _handler_wrapper(wrapper: RequestWrapper):
            response = await call_http_handler(wrapper.http_request, handler)
            try:
                if isinstance(response, list):
                    return web.json_response([o.dict() for o in response])

                return web.json_response(response.dict())
            except AttributeError:
                return response

        return _handler_wrapper


app = MyApp()
