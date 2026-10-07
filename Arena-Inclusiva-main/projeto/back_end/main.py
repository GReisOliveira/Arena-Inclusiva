from fastapi import FastAPI

from src.controllers.usuarios_routes import router as usuarios_router

app = FastAPI(title="Arena Inclusiva API")

app.include_router(usuarios_router)


@app.get("/health", tags=["Health"])
async def health() -> dict[str, str]:
    return {"status": "ok"}
