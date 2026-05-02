from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base

class CountryTable(Base):
    __tablename__ = "countries"
    
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    image_base64: Mapped[str | None] = mapped_column(String(1000))

    def __repr__(self) -> str:
        return f"<CountryTable(name={self.name!r}, code={self.code!r})>"