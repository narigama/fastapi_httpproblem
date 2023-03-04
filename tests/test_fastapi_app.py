import fastapi


async def test_returns_200(client):
    response = await client.get("/returns_200")

    assert response.status_code == fastapi.status.HTTP_200_OK
    assert response.json() == {"ok": True}


async def test_returns_404_with_no_detail(client):
    response = await client.get("/returns_404_with_no_detail")

    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
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

    assert response.status_code == fastapi.status.HTTP_404_NOT_FOUND
    assert response.headers["Content-Type"] == "application/problem+json"
    assert response.json() == {
        "status": 404,
        "title": "The User could not be located.",
        "detail": "User foo@bar.com was not found.",
        "type": "http://localhost/problem/user-not-found",
        "instance": "http://localhost/returns_404_with_detail",
    }
