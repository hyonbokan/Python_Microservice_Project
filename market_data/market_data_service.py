from utils.interfaces import DatabaseService, CacheService

class MarketDataService:
    def __init__(self, cache: CacheService, database: DatabaseService):
        self.cache = cache
        self.database = database
    
    async def get_market_data(self):
        data = await self.database.fetch_trade_data()
        return data