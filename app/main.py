from fastapi import FastAPI

app = FastAPI(
    title="My PoC Banking API",
    description="API com divisao de rotas Cliente (v1) e Admin",
    version="1.0.0"
)

import api.v1.base as v1_router
import api.admin.base as admin_router

app.include_router(v1_router.router)
app.include_router(admin_router.router)

