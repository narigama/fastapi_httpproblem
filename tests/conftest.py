import async_asgi_testclient
import fastapi
import fastapi.testclient
import pytest

import fastapi_httpproblem


@pytest.fixture()
async def app():
    app = fastapi.FastAPI()
    fastapi_httpproblem.install_error_handler(app)

    class UserNotFound(fastapi_httpproblem.Problem):
        status = 404
        kind = "user-not-found"
        title = "The User could not be located."

    @app.get("/returns_200")
    async def returns_200():
        return { "ok": True }

    @app.get("/returns_404_with_no_detail")
    async def returns_404_with_no_detail():
        raise UserNotFound()

    @app.get("/returns_404_with_detail")
    async def returns_404_with_detail():
        raise UserNotFound("User foo@bar.com was not found.")

    @app.get("/returns_500_uncaught_exception")
    async def returns_500_uncaught_exception():
        1 / 0  # ZeroDivisionError, should get remapped to UncaughtException()

    yield app


@pytest.fixture()
async def client(app):  # noqa: D103
    async with async_asgi_testclient.TestClient(app) as client:
        yield client
