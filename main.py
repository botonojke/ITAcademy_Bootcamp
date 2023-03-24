import uvicorn
from fastapi import FastAPI

from core.config import WEB_PORT, WEB_HOST
from db.base import database
from endpoints import author, books

app = FastAPI(title="MY_APP")
app.include_router(author.router, prefix="/author", tags=["author"])
app.include_router(books.router, prefix="/books", tags=["books"])


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


@app.get("/")
async def read_root():
    return {"Hello": "World"}


if __name__ == "__main__":
    uvicorn.run("main:app", port=int(WEB_PORT), host=WEB_HOST, reload=True)
