import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import asyncio
from aiohttp import web
from database.market_postgres_service import PostgreSQLMarketService
from cache.redis_cache import RedisCacheService
from market_data_service import MarketDataService
from message_queue.rabbitmq_service import RabbitMQService

cache = RedisCacheService()
database = PostgreSQLMarketService(cache=cache)
publisher = RabbitMQService()
market_service = MarketDataService(cache=cache, database=database, publisher=publisher)

async def market_data_handler(request):
    data = await market_service.get_market_data()
    return web.json_response({"data": data})


async def init_app():
    app = web.Application()
    app.router.add_get('/market-data', market_data_handler)
    return app

if __name__ == "__main__":
    app = asyncio.run(init_app())
    web.run_app(app, host="0.0.0.0", port=5001)