from fastapi import FastAPI

from . import models
from .database import engine
from .routers import user, auth

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


app.include_router(auth.router)
app.include_router(user.router)
