from fastapi import FastAPI

from main.routers import player, pair

app = FastAPI()

app.include_router(player.router)
app.include_router(pair.router)


@app.get("/ping")
def ping_app():
    return "Is anybody home?"
