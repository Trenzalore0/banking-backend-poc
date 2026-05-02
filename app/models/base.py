from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped, mapped_column

class Base(DeclarativeBase):
    # Isso adiciona o ID automaticamente em todos os modelos que herdarem de Base
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    pass


#from .user import User
#from .country import Country
#from .currency import Currency
#from .balance import Balance
