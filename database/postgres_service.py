from utils.interfaces import DatabaseService, CacheService
from sqlalchemy.future import select
from database.models.models_market_data import MarketData
from database.models.base import SessionLocal

class PostgreSQLService(DatabaseService):
    def __init__(self, cache: CacheService):
        self.cache = cache
    
    async def fetch_trade_data(self):
        cache_data = self.cache.get("latest_market_data")
        if cache_data:
            return cache_data
        
        async with SessionLocal() as session:
            async with session.begin():
                stmt = select(MarketData).order_by(MarketData.timestamp.desc()).limit(10)
                result = await session.execute(stmt)
                records = result.scalars().all()
                
                data = [
                    dict(id=record.id, market=record.market, price=record.price, timestamp=record.timestamp.isoformat())
                    for record in records
                ]
                
                self.cache.save("latest_market_data", data)
                return data
    
    async def save_trade_data(self, market, price, timestamp):
        async with SessionLocal() as session:
            async with session.begin():
                trade = MarketData(market=market, price=price, timestamp=timestamp)
                session.add(trade)