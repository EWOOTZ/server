from fastapi import FastAPI

from . import models
from .database import engine
from .routers import (
    user,
    auth,
    dialog,
    qna,
    wish,
    upload,
    download,
    mailbox,
    follow,
    youtube,
    search,
    board,
    game,
)
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import FileResponse
from starlette.staticfiles import StaticFiles

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = [
    "http://ewootz.site:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://ewootz.site:3000"],  # 클라이언트의 URL
    allow_credentials=True,
    allow_methods=["*"],  # 모든 HTTP 메소드 허용
    allow_headers=["*"],  # 모든 HTTP 헤더 허용
)


@app.get("/")
def index():
    return FileResponse("/home/ubuntu/client/build/index.html")


app.mount("/static", StaticFiles(directory="/home/ubuntu/client/build/static"))

app.include_router(auth.router)
app.include_router(user.router)
app.include_router(dialog.router)
app.include_router(qna.router)
app.include_router(upload.router)
app.include_router(download.router)
app.include_router(wish.router)
app.include_router(mailbox.router)
app.include_router(follow.router)
app.include_router(youtube.router)
app.include_router(search.router)
app.include_router(board.router)
app.include_router(game.router)
