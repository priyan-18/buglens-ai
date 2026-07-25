from fastapi import FastAPI

from app.api.router import api_router

app = FastAPI(
    title="BugLens AI API",
    description="Enterprise AI-powered defect intelligence platform API.",
    version="1.0.0",
)

app.include_router(api_router, prefix="/api/v1")


@app.get("/", tags=["Root"])
async def root() -> dict[str, str]:
    """Return basic API information."""
    return {
        "name": "BugLens AI API",
        "version": "1.0.0",
        "documentation": "/docs",
    }