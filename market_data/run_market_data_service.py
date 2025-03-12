import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))
import asyncio
from aiohttp import web
from database.postgres_service import PostgreSQLService
from cache.redis_cache import RedisCacheService
from market_data_service import MarketDataService

cache = RedisCacheService()
database = PostgreSQLService(cache=cache)
market_service = MarketDataService(cache=cache, database=database)

async def market_data_handler(request):
    data = await market_service.get_market_data()
    return web.json_response({"data": data})


async def init_app():
    app = web.Application()
    app.router.add_get('/market-data', market_data_handler)
    return app

if __name__ == "__main__":
    app = asyncio.run(init_app())
    web.run_app(app, host="0.0.0.0", port=5000)