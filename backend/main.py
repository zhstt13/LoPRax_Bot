from fastapi import FastAPI

app = FastAPI(title="LoPRax API")


@app.get("/health")
async def health():
    return {"status": "ok"}
