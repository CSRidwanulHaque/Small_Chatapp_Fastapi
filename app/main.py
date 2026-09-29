from fastapi import FastAPI
from app.routers.routers import router as users_router

app = FastAPI(title="Small Chat App")
app.include_router(users_router)


@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok"}
