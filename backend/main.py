from fastapi import FastAPI

from backend.api.router import router

app = FastAPI(title="LoPRax API")

app.include_router(router)


@app.get("/health")
async def health():
    return {"status": "ok"}
