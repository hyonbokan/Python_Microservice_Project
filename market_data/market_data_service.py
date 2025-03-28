from utils.interfaces import MarketDatabaseService, CacheService, MessageQueueService

class MarketDataService:
    def __init__(self, cache: CacheService, database: MarketDatabaseService, publisher: MessageQueueService):
        self.cache = cache
        self.database = database
        self.publisher = publisher
    
    async def get_market_data(self):
        data = await self.database.fetch_trade_data()
        return data
    
    async def create_market_data(self, market, price, timestamp):
        await self.database.save_trade_data(market=market, price=price, timestamp=timestamp)
        message = {
            "market": market,
            "price": price,
            "timestamp": timestamp.isoformat()
            }
        self.publisher.publish_message(message=message)