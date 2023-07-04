from fastapi import FastAPI
from tortoise import fields
from tortoise.models import Model
from tortoise.contrib.fastapi import register_tortoise
from pydantic import BaseModel

app = FastAPI()


class User(Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=100)
    email = fields.CharField(max_length=100)

    class Meta:
        table = "users"


class UserCreateRequest(BaseModel):
    name: str
    email: str


@app.get("/users")
async def get_users():
    users = await User.all().values()
    return {"users": users}


@app.post("/users")
async def create_user(user_data: UserCreateRequest):
    user = await User.create(name=user_data.name, email=user_data.email)
    return {"message": "User created successfully", "user": user}


register_tortoise(
    app,
    db_url="sqlite://database//db.sqlite3",
    modules={"models": ["main"]},
    generate_schemas=True,
    add_exception_handlers=True,
)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8099)
