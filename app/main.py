from fastapi import FastAPI

app = FastAPI(
    title="My PoC Banking API",
    description="API com divisao de rotas Cliente (v1) e Admin",
    version="1.0.0"
)

from app.api.v1.base import router as v1_router
from app.api.admin.base import router as admin_router

app.include_router(v1_router)
app.include_router(admin_router)

