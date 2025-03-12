from sqlalchemy import Column, Integer, String, Float, TIMESTAMP
from database.models import Base

class MarketData(Base):
    __tablename__ = "market_data"

    id = Column(Integer, primary_key=True, index=True)
    market = Column(String, nullable=False)
    price = Column(Float, nullable=False)
    timestamp = Column(TIMESTAMP, nullable=False)