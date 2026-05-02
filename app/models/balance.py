from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import String
from .base import Base

class BalanceTable(Base):
    __tablename__ = "balances"

    user_id: Mapped[int] = mapped_column(nullable=False)
    currency_id: Mapped[int] = mapped_column(nullable=False)
    amount: Mapped[float] = mapped_column(nullable=False)

    def __repr__(self) -> str:
        return f"<BalanceTable(user_id={self.user_id!r}, currency_id={self.currency_id!r}, amount={self.amount!r})>"
    