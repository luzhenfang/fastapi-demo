from fastapi import FastAPI

from application.routers import users


def register(app: FastAPI):
    app.include_router(users.router)
