from http import HTTPStatus

from asynctest import TestCase
from asyncworker.testing import HttpClientContext

from baas.api import app


class AccountAPITest(TestCase):
    async def test_health(self):
        async with HttpClientContext(app) as client:
            resp = await client.get("/health")

            self.assertEqual(HTTPStatus.OK, resp.status)
            data = await resp.json()
            self.assertEqual({"OK": True}, data)
