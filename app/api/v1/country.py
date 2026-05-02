from fastapi import Depends, HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from database import get_db
from models.country import CountryTable

from pydantic import BaseModel

class CountrySearch(BaseModel):
    country: dict = {
        "id": 0,
        "name": "",
        "code": ""
    }

from .base import router

@router.get("/countries")
async def get_countries(db: AsyncSession = Depends(get_db)):
    query = select(CountryTable).order_by(CountryTable.id)
    result = await db.execute(query)
    countries = result.scalars().all()
    return {"countries": [country.name for country in countries]}

@router.post("/countries/id/")
async def get_country(country: CountrySearch, db: AsyncSession = Depends(get_db)):
    query = select(CountryTable).where(CountryTable.id == country.country["id"])
    result = await db.execute(query)
    country = result.scalar_one_or_none()
    if country is None:
        raise HTTPException(status_code=404, detail="Country not found")
    return {"country_id": country.id, "name": country.name, "code": country.code}

@router.get("/countries/name/{country_name}")
async def get_country_by_name(country_name: str, db: AsyncSession = Depends(get_db)):
    query = select(CountryTable).where(CountryTable.name == country_name)
    result = await db.execute(query)
    country = result.scalar_one_or_none()
    return {"search_country_name": country_name, "result_name": country.name}
