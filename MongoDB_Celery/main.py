import uvicorn as uvicorn
from fastapi import FastAPI

from config.celery_utils import create_celery
from routers import chats


def create_app() -> FastAPI:
    current_app = FastAPI(title="Asynchronous tasks processing with Celery and Redis",
                          description="FastAPI Application to store the chat history with Celery and Redis",
                          version="1.0.0",)

    current_app.celery_app = create_celery()
    current_app.include_router(chats.router)
    return current_app


app = create_app()
celery = app.celery_app

if __name__ == "__main__":
    uvicorn.run("main:app", port=9000, reload=True)