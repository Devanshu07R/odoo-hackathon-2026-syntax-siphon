from fastapi import FastAPI

from app.api.auth import router as auth_router

app = FastAPI(
    title="AssetFlow ERP",
    version="1.0.0",
)

# Register API Routers
app.include_router(auth_router)


@app.get("/")
def root():
    return {
        "message": "AssetFlow ERP API is running 🚀"
    }