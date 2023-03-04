# fastapi_httpproblem

This library implements [RFC7807](https://www.rfc-editor.org/rfc/rfc7807)
for FastAPI applications.

After installing it, use the following snippet to get started:

```python
import fastapi
import fastapi_httpproblem


app = fastapi.FastAPI()

# install the middleware to automatically handle Problems
fastapi_httpproblem.install(app)


# define your own classes that extend fastapi_httpproblem.Problem
class UserNotFound(fastapi_httpproblem.Problem):
    status = 404
    kind = "user-not-found"
    title = "User was not found."


@app.get("/user/{user_id:int}")
async def user_get_by_id(user_id: int):
    user = query.user_get_by_id(user_id)

    # raise the Problem to automatically return a http problem
    if not user:
        message = "User with ID: {} was not found"
        raise UserNotFound(message.format(user_id))

    return user
```

