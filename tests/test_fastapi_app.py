async def test_returns_200(client):
    response = await client.get("/returns_200")

    assert response.status_code == 200
    assert response.json() == {"ok": True}


async def test_returns_404_with_no_detail(client):
    response = await client.get("/returns_404_with_no_detail")

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/problem+json"
    assert response.json() == {
        "status": 404,
        "title": "The User could not be located.",
        "detail": "No detail provided",
        "type": "http://localhost/problem/user-not-found",
        "instance": "http://localhost/returns_404_with_no_detail",
    }

async def test_returns_404_with_detail(client):
    response = await client.get("/returns_404_with_detail")

    assert response.status_code == 404
    assert response.headers["Content-Type"] == "application/problem+json"
    assert response.json() == {
        "status": 404,
        "title": "The User could not be located.",
        "detail": "User foo@bar.com was not found.",
        "type": "http://localhost/problem/user-not-found",
        "instance": "http://localhost/returns_404_with_detail",
    }

async def test_returns_500_uncaught_error(client):
    response = await client.get("/returns_500_uncaught_exception")

    assert response.status_code == 500
    assert response.headers["Content-Type"] == "application/problem+json"
    assert response.json() == {
        "status": 500,
        "title": "The Server experienced an unexpected problem.",
        "detail": "ZeroDivisionError",
        "type": "http://localhost/problem/uncaught-exception",
        "instance": "http://localhost/returns_500_uncaught_exception",
    }
