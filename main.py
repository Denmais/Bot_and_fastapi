from fastapi.responses import JSONResponse
from fastapi import FastAPI
import sheme
from bot import send

app = FastAPI()


@app.post("/message")
async def read_root(message: sheme.Base):
    await send(message.message)
    return JSONResponse(status_code=200, content={})
