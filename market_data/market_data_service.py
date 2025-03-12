from utils.interfaces import MarketDatabaseService, CacheService

class MarketDataService:
    def __init__(self, cache: CacheService, database: MarketDatabaseService):
        self.cache = cache
        self.database = database
    
    async def get_market_data(self):
        data = await self.database.fetch_trade_data()
        return data