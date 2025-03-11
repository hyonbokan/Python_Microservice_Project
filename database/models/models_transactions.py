from sqlalchemy import Column, Integer, Float, String, TIMESTAMP, func
from database.models import Base

class TransactionData(Base):
    __tablename__ = 'transaction_data'

    id = Column(Integer, primary_key=True, index=True)
    order_id = Column(String, nullable=False)
    product = Column(String, nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    price = Column(Float, nullable=False)
    status = Column(String, nullable=False, default='PENDING')
    timestamp = Column(TIMESTAMP, nullable=False, server_default=func.now())
