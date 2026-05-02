from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base

class CurrencyTable(Base):
    __tablename__ = "currencies"

    country_id: Mapped[int] = mapped_column(nullable=False)
    name: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    code: Mapped[str] = mapped_column(String(10), unique=True, nullable=False)
    symbol: Mapped[str] = mapped_column(String(10), nullable=False)

    def __repr__(self) -> str:
        return f"<CurrencyTable(name={self.name!r}, code={self.code!r})>"