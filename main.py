from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
import uuid

from starlette.websockets import WebSocket

app = FastAPI(
    title="Apis task 6",
    version="0.0.1"
)

@app.post("/api/v1/users")
async def create_user(username: str, name: str):
    return {
        "username": username,
        "name": name,
        "id": str(uuid.uuid4()),
        "message": "User created successfully",
        "status_code": 201
    }

@app.get("/api/v1/{user_id}")
async def create_user(user_id: str):
    users = {
        "hola123": {
            "username": "hola123",
            "name": "Gabo"
        }
    }


    if user_id in users:

        user = users[user_id]

        return JSONResponse(
            content=user,
            status_code=status.HTTP_200_OK)
    else:
        return JSONResponse(
            content="User not found",
            status_code=status.HTTP_404_NOT_FOUND
        )

