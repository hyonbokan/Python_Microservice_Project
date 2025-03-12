from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession
from database.models import TransactionData
from database.models.base import SessionLocal
from utils.interfaces import TransactionDatabaseService

class PostgreSQLTransactionService(TransactionDatabaseService):
    async def fetch_transaction_data(self):
        async with SessionLocal() as session:
            async with session.begin():
                stmt = select(TransactionData).order_by(TransactionData.timestamp.desc()).limit(10)
                result = await session.execute(stmt)
                records = result.scalars().all()
                data = [
                    {
                        "id": record.id,
                        "order_id": record.order_id,
                        "product": record.product,
                        "quantity": record.quantity,
                        "price": record.price,
                        "status": record.status,
                        "timestamp": record.timestamp.isoformat() if record.timestamp else None,
                    }
                    for record in records
                ]
                return data
    
    async def save_transaction_data(self, order_id, product, quantity, price, status, timestamp):
        async with SessionLocal() as session:
            async with session.begin():
                new_transaction = TransactionData(
                    order_id=order_id,
                    product=product,
                    quantity=quantity,
                    price=price,
                    status=status,
                    timestamp=timestamp
                )
                session.add(new_transaction)