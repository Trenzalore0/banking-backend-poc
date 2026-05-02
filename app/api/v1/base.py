from fastapi import APIRouter

router = APIRouter(
    prefix="/api/v1",
    tags=["v1"]
)

import api.v1.country
